from abc import ABC, abstractmethod

from apps.teams.entities.team_entity import TeamEntity


class TeamRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[TeamEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_code(self, team_code: str) -> TeamEntity | None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, team_code: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def add(self, team: TeamEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update(self, team: TeamEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, team_code: str) -> bool:
        raise NotImplementedError
