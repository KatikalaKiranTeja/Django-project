from abc import ABC, abstractmethod

from apps.players.dtos.player_dto import CreatePlayerDTO, UpdatePlayerDTO
from apps.players.entities.player_entity import PlayerEntity


class PlayerService(ABC):
    @abstractmethod
    def get_all_players(self) -> list[PlayerEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_player(self, jersey_number: int, team_code: str) -> PlayerEntity | None:
        raise NotImplementedError

    @abstractmethod
    def create_player(self, dto: CreatePlayerDTO) -> tuple[bool, str]:
        raise NotImplementedError

    @abstractmethod
    def update_player(self, dto: UpdatePlayerDTO) -> tuple[bool, str]:
        raise NotImplementedError

    @abstractmethod
    def delete_player(self, jersey_number: int, team_code: str) -> tuple[bool, str]:
        raise NotImplementedError
