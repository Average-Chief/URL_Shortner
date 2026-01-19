from fastapi import FastAPI
from db import engine
from models import create_db
from routes import router

app = FastAPI(title = "URL Shortener Service")

@app.on_event("startup")
def on_startup():
    create_db(engine)

app.include_router(router)

