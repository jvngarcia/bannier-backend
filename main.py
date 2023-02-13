from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()



# Importa las rutas del aplicativo
from app.v1.router import GenerateBackground


app = FastAPI()
app.include_router( GenerateBackground.router )