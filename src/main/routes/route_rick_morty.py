from fastapi import APIRouter

rick_morty_router = APIRouter()


@rick_morty_router.get("/rm/episode/{id}")
def get_episode(id: int):
    return {"id": id}
