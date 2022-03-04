from fastapi import APIRouter
from src.api_colector.api_colector import RickMortyApiColector

rick_morty_router = APIRouter()


@rick_morty_router.get("/rm/episode/{id}")
def get_episode(id: int):
    info_episode = RickMortyApiColector().info_episode(id)
    return info_episode


@rick_morty_router.get("/rm/episode/{id}")
def get_character(id: int):
    info_episode = RickMortyApiColector().info_episode(id)
    return info_episode
