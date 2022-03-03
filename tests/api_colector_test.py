from src.infra.api_consumer import RickMortyApiConsumer
from src.api_colector import RickMortyApiColector


def test_info_episode():
    id_episode = 2
    rm_api_colector = RickMortyApiColector(RickMortyApiConsumer())
    response_api_colector = rm_api_colector.info_episode(id_episode)

    assert (
        response_api_colector.request.url
        == f"https://rickandmortyapi.com/api/episode/{id_episode}"
    )
    assert response_api_colector.status_code == 200
