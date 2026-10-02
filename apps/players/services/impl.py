from apps.players.dtos.player_dto import CreatePlayerDTO, UpdatePlayerDTO
from apps.players.entities.player_entity import PlayerEntity
from apps.players.repositories.impl import PlayerRepositoryImpl
from apps.players.services.interfaces import PlayerService


class PlayerServiceImpl(PlayerService):
    def __init__(self) -> None:
        self.repo = PlayerRepositoryImpl()

    def get_all_players(self) -> list[PlayerEntity]:
        return self.repo.list_all()

    def get_player(self, jersey_number: int, team_code: str) -> PlayerEntity | None:
        return self.repo.get_by_jersey(jersey_number, team_code)

    def create_player(self, dto: CreatePlayerDTO) -> tuple[bool, str]:
        if self.repo.get_by_jersey(dto.jersey_number, dto.team_code):
            return False, 'duplicate'
        entity = PlayerEntity(dto.jersey_number, dto.player_name, dto.age, dto.role, dto.nationality, dto.team_code, dto.image_path)
        return (True, 'success') if self.repo.add(entity) else (False, 'error')

    def update_player(self, dto: UpdatePlayerDTO) -> tuple[bool, str]:
        entity = PlayerEntity(dto.jersey_number, dto.player_name, dto.age, dto.role, dto.nationality, dto.team_code, dto.image_path)
        return (True, 'updated') if self.repo.update(entity) else (False, 'error')

    def delete_player(self, jersey_number: int, team_code: str) -> tuple[bool, str]:
        return (True, 'deleted') if self.repo.delete(jersey_number, team_code) else (False, 'error')
