from src.infra.api_consumer import RickMortyApiConsumer


def test_get_episode():
    id_episode = 2
    episodes = RickMortyApiConsumer().get_episode(id_episode)

    assert episodes.request.method == "GET"
    assert (
        episodes.request.url == f"https://rickandmortyapi.com/api/episode/{id_episode}"
    )
    assert episodes.status_code == 200
    assert isinstance(episodes.response, dict)


def test_get_character():
    id_character = 2
    character = RickMortyApiConsumer().get_character(id_character)

    assert character.request.method == "GET"
    assert (
        character.request.url
        == f"https://rickandmortyapi.com/api/character/{id_character}"
    )
    assert character.status_code == 200
    assert isinstance(character.response, dict)
