from dataclasses import dataclass


@dataclass
class TeamEntity:
    team_code: str
    team_name: str
    country: str
    coach_name: str
    captain_name: str
    logo_path: str
