import requests
from requests import Request
from typing import Type, Tuple, Dict
from collections import namedtuple


class RickMortyApiConsumer:
    def __init__(self):
        self.get_response = namedtuple("GET_INFO", "status_code request response")

    def get_episode(self, id_episode: int) -> Tuple[int, Type[Request], Dict]:
        """Retorna informações sobre um episódio.

        :param id_episode: id do episodio.
        :return: Tuple[int, Type[Request], Dict]
        """
        request = requests.Request(
            method="GET", url=f"https://rickandmortyapi.com/api/episode/{id_episode}"
        )
        response = self.__send_http_request(request.prepare())
        return self.get_response(
            status_code=response.status_code, request=request, response=response.json()
        )

    def get_character(self, id_character):
        request = requests.Request(
            method="GET",
            url=f"https://rickandmortyapi.com/api/character/{id_character}",
        )
        response = self.__send_http_request(request.prepare())
        return self.get_response(
            status_code=response.status_code, request=request, response=response.json()
        )

    @classmethod
    def __send_http_request(cls, request_prepared: Type[Request]):
        http_session = requests.Session()
        return http_session.send(request_prepared)
