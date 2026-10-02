from dataclasses import dataclass


@dataclass
class UpsertMatchDTO:
    match_id: int
    team1_code: str
    team2_code: str
    venue: str
    match_date: str
    match_time: str
    status: str
    winner_code: str
    team1_score: str
    team2_score: str
    player_of_match: str
