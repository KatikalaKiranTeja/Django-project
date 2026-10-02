from dataclasses import dataclass


@dataclass
class CreatePlayerDTO:
    jersey_number: int
    player_name: str
    age: int
    role: str
    nationality: str
    team_code: str
    image_path: str


@dataclass
class UpdatePlayerDTO:
    jersey_number: int
    player_name: str
    age: int
    role: str
    nationality: str
    team_code: str
    image_path: str
