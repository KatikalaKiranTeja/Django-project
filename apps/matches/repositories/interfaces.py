from abc import ABC, abstractmethod

from apps.matches.entities.match_entity import MatchEntity


class MatchRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[MatchEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, match_id: int) -> MatchEntity | None:
        raise NotImplementedError

    @abstractmethod
    def add(self, match: MatchEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update(self, match: MatchEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, match_id: int) -> bool:
        raise NotImplementedError
