from fastapi import FastAPI
from src.main.routes.route_rick_morty import rick_morty_router

app = FastAPI()

app.include_router(rick_morty_router)
