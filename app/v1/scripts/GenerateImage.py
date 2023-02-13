import os
import base64
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


class GenerateImage:

    def initialize_api():
        os.environ['STABILITY_HOST'] = os.getenv('STABILITY_HOST')

        os.environ['STABILITY_KEY'] = os.getenv('STABILITY_KEY')

        return client.StabilityInference(
            key = os.environ['STABILITY_KEY'] ,
            verbose=True,
            engine="stable-diffusion-v1-5",
        )

    def prepare( background, type ):
        

        # Set up our connection to the API.
        stability_api = GenerateImage.initialize_api()

        return stability_api.generate(
            prompt = [
                generation.Prompt(text = background, parameters=generation.PromptParameters(weight=1)),
                generation.Prompt(text = type, parameters=generation.PromptParameters(weight=1.5))
            ],
            seed=5054264,
            steps=15,
            cfg_scale=7.0,
            width=512, 
            height=512, 
            samples=1,
            sampler=generation.SAMPLER_K_DPMPP_2M
        )


    @staticmethod
    def images( background, type ):

        answers = GenerateImage.prepare( background, type )

        images = []

        for resp in answers:
            for artifact in resp.artifacts: 
                if artifact.finish_reason == generation.FILTER:
                    return False
                    
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    images.append( base64.b64encode( artifact.binary ).decode() )
                    img.save(str(artifact.seed)+ ".png") # Save our generated images with their seed number as the filename.
        
        return images



