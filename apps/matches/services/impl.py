from apps.matches.dtos.match_dto import UpsertMatchDTO
from apps.matches.entities.match_entity import MatchEntity
from apps.matches.repositories.impl import MatchRepositoryImpl
from apps.matches.services.interfaces import MatchService


class MatchServiceImpl(MatchService):
    def __init__(self) -> None:
        self.repo = MatchRepositoryImpl()

    def list_matches(self) -> list[MatchEntity]:
        return self.repo.list_all()

    def get_match(self, match_id: int) -> MatchEntity | None:
        return self.repo.get_by_id(match_id)

    def create_match(self, dto: UpsertMatchDTO) -> tuple[bool, str]:
        entity = MatchEntity(**dto.__dict__)
        return (True, 'success') if self.repo.add(entity) else (False, 'error')

    def update_match(self, dto: UpsertMatchDTO) -> tuple[bool, str]:
        existing = self.repo.get_by_id(dto.match_id)
        if not existing:
            return False, 'error'

        # Prevent nulling critical fields for completed match edits.
        if (existing.status or '').lower() == 'completed':
            dto.team1_code = dto.team1_code or existing.team1_code
            dto.team2_code = dto.team2_code or existing.team2_code
            dto.venue = dto.venue or existing.venue
            dto.match_date = dto.match_date or existing.match_date
            dto.match_time = dto.match_time or existing.match_time

        entity = MatchEntity(**dto.__dict__)
        return (True, 'updated') if self.repo.update(entity) else (False, 'error')

    def delete_match(self, match_id: int) -> tuple[bool, str]:
        return (True, 'deleted') if self.repo.delete(match_id) else (False, 'error')
