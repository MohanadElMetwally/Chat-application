from fastapi import FastAPI
from app.controllers.api_controller import router

app = FastAPI()
app.include_router(router)