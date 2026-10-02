from dataclasses import dataclass


@dataclass
class PlayerEntity:
    jersey_number: int
    player_name: str
    age: int
    role: str
    nationality: str
    team_code: str
    image_path: str
