from fastapi import APIRouter, HTTPException
import os
from app.v1.scripts.GenerateImage import GenerateImage

from app.v1.schema import GenerateBackgroundSchema


router = APIRouter( prefix = '/api/v1/generate-background', tags = [''] )

class GenerateBackground:

    @router.get('/') 
    async def index( ):



        img = GenerateImage.images('Elefante', 'realistic')

        if img == False:
            raise HTTPException(status_code=404, detail="Your request activated the safety filters and could not be processed. Please modify the prompt and try again.")

        return {'images': img}