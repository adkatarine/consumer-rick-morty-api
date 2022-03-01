from src.infra.api_consumer.rick_morty_api_consumer import RickMortyApiConsumer


def test_get_episode():
    id_episode = 2
    episodes = RickMortyApiConsumer().get_episode(id_episode)

    assert episodes.request.method == "GET"
    assert (
        episodes.request.url == f"https://rickandmortyapi.com/api/episode/{id_episode}"
    )
    assert episodes.status_code == 200
    assert isinstance(episodes.response, dict)
