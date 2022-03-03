from src.api_colector import RickMortyApiColector


def test_info_episode():
    id_episode = 2
    response_api_colector = RickMortyApiColector().info_episode(id_episode)

    assert isinstance(response_api_colector, dict)
