from apps.teams.dtos.team_dto import CreateTeamDTO, UpdateTeamDTO
from apps.teams.entities.team_entity import TeamEntity
from apps.teams.repositories.impl import TeamRepositoryImpl
from apps.teams.services.interfaces import TeamService


class TeamServiceImpl(TeamService):
    def __init__(self) -> None:
        self.repo = TeamRepositoryImpl()

    def get_all_teams(self) -> list[TeamEntity]:
        return self.repo.list_all()

    def get_team(self, team_code: str) -> TeamEntity | None:
        return self.repo.get_by_code(team_code)

    def create_team(self, dto: CreateTeamDTO) -> tuple[bool, str]:
        if self.repo.exists(dto.team_code):
            return False, 'duplicate'
        entity = TeamEntity(
            team_code=dto.team_code,
            team_name=dto.team_name,
            country=dto.country,
            coach_name=dto.coach_name,
            captain_name=dto.captain_name,
            logo_path=dto.logo_path,
        )
        return (True, 'success') if self.repo.add(entity) else (False, 'error')

    def update_team(self, dto: UpdateTeamDTO) -> tuple[bool, str]:
        entity = TeamEntity(
            team_code=dto.team_code,
            team_name=dto.team_name,
            country=dto.country,
            coach_name=dto.coach_name,
            captain_name=dto.captain_name,
            logo_path=dto.logo_path,
        )
        return (True, 'updated') if self.repo.update(entity) else (False, 'error')

    def delete_team(self, team_code: str) -> tuple[bool, str]:
        return (True, 'deleted') if self.repo.delete(team_code) else (False, 'error')
