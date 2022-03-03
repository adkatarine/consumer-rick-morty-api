from src.infra.api_consumer import RickMortyApiConsumer
from typing import Type


class RickMortyApiColector:
    def __init__(self, rm_api_consumer: Type[RickMortyApiConsumer]) -> None:
        self.rm_api_consumer = rm_api_consumer

    def info_episode(self, id_episode: int) -> dict:
        rm_api_response = self.rm_api_consumer.get_episode(id_episode)
        return rm_api_response
