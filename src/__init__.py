from src.infra.api_consumer import RickMortyApiConsumer
from src.api_colector import RickMortyApiColector

id_episode = 2
rm_api_colector = RickMortyApiColector(RickMortyApiConsumer())
response_api_colector = rm_api_colector.info_episode(id_episode)

print(response_api_colector)
