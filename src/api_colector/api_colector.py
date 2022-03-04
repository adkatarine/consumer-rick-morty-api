from src.infra.api_consumer import RickMortyApiConsumer


class RickMortyApiColector:
    def __init__(self) -> None:
        self.rm_api_consumer = RickMortyApiConsumer()

    def info_episode(self, id_episode: int) -> dict:
        rm_api_response = self.rm_api_consumer.get_episode(id_episode)
        return self.format_info_episode(rm_api_response)

    def info_character(self, id_character: int) -> dict:
        rm_api_response = self.rm_api_consumer.get_character(id_character)
        return self.format_info_character(rm_api_response)

    def format_info_episode(self, episode: dict):
        formated_ep = {
            "id": episode.response["id"],
            "name": episode.response["name"],
            "episode": episode.response["episode"],
            "air_date": episode.response["air_date"],
            "characters": self.update_characters_ep(episode.response["characters"]),
        }
        return formated_ep

    def format_info_character(self, character: dict):
        return {
            "name": character.response["name"],
            "status": character.response["status"],
            "image": character.response["image"],
        }

    def update_characters_ep(self, characters):
        return [
            self.info_character(character.split("/")[-1]) for character in characters
        ]
