import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from src.database import engine, Base
from src.routes import router 

load_dotenv()
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)
