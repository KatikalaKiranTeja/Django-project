from abc import ABC, abstractmethod

from apps.teams.dtos.team_dto import CreateTeamDTO, UpdateTeamDTO
from apps.teams.entities.team_entity import TeamEntity


class TeamService(ABC):
    @abstractmethod
    def get_all_teams(self) -> list[TeamEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_team(self, team_code: str) -> TeamEntity | None:
        raise NotImplementedError

    @abstractmethod
    def create_team(self, dto: CreateTeamDTO) -> tuple[bool, str]:
        raise NotImplementedError

    @abstractmethod
    def update_team(self, dto: UpdateTeamDTO) -> tuple[bool, str]:
        raise NotImplementedError

    @abstractmethod
    def delete_team(self, team_code: str) -> tuple[bool, str]:
        raise NotImplementedError
