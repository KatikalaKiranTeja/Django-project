from dataclasses import dataclass


@dataclass
class CreateTeamDTO:
    team_code: str
    team_name: str
    country: str
    coach_name: str
    captain_name: str
    logo_path: str


@dataclass
class UpdateTeamDTO:
    team_code: str
    team_name: str
    country: str
    coach_name: str
    captain_name: str
    logo_path: str
