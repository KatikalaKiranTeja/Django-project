from abc import ABC, abstractmethod

from apps.players.entities.player_entity import PlayerEntity


class PlayerRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[PlayerEntity]:
        raise NotImplementedError

    @abstractmethod
    def list_by_team(self, team_code: str) -> list[PlayerEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_jersey(self, jersey_number: int, team_code: str) -> PlayerEntity | None:
        raise NotImplementedError

    @abstractmethod
    def add(self, player: PlayerEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update(self, player: PlayerEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, jersey_number: int, team_code: str) -> bool:
        raise NotImplementedError
