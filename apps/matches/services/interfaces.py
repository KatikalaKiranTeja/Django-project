from abc import ABC, abstractmethod

from apps.matches.dtos.match_dto import UpsertMatchDTO
from apps.matches.entities.match_entity import MatchEntity


class MatchService(ABC):
    @abstractmethod
    def list_matches(self) -> list[MatchEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_match(self, match_id: int) -> MatchEntity | None:
        raise NotImplementedError

    @abstractmethod
    def create_match(self, dto: UpsertMatchDTO) -> tuple[bool, str]:
        raise NotImplementedError

    @abstractmethod
    def update_match(self, dto: UpsertMatchDTO) -> tuple[bool, str]:
        raise NotImplementedError

    @abstractmethod
    def delete_match(self, match_id: int) -> tuple[bool, str]:
        raise NotImplementedError
