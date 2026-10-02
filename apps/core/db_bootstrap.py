from __future__ import annotations

from django.db import connection


def ensure_sqlite_schema() -> None:
    """Create core tables when using SQLite and they do not exist yet."""
    if connection.vendor != "sqlite":
        return

    with connection.cursor() as cursor:
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='teams'"
        )
        if cursor.fetchone():
            return

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS teams (
                teamCode TEXT PRIMARY KEY,
                teamName TEXT NOT NULL,
                country TEXT NOT NULL DEFAULT 'India',
                coachName TEXT NOT NULL,
                captainName TEXT NOT NULL,
                logoPath TEXT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS players (
                jerseyNumber INTEGER NOT NULL,
                playerName TEXT NOT NULL,
                age INTEGER NOT NULL,
                role TEXT NOT NULL,
                nationality TEXT NOT NULL,
                teamCode TEXT NOT NULL,
                imagePath TEXT NULL,
                PRIMARY KEY (jerseyNumber, teamCode),
                FOREIGN KEY (teamCode) REFERENCES teams(teamCode)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS matches (
                match_id INTEGER PRIMARY KEY,
                match_date TEXT NULL,
                match_time TEXT NULL,
                team1_code TEXT NULL,
                team2_code TEXT NULL,
                venue TEXT NULL,
                status TEXT NOT NULL,
                winner_code TEXT NULL,
                team1_score TEXT NULL,
                team2_score TEXT NULL,
                player_of_match TEXT NULL,
                FOREIGN KEY (team1_code) REFERENCES teams(teamCode)
                    ON UPDATE CASCADE ON DELETE SET NULL,
                FOREIGN KEY (team2_code) REFERENCES teams(teamCode)
                    ON UPDATE CASCADE ON DELETE SET NULL,
                FOREIGN KEY (winner_code) REFERENCES teams(teamCode)
                    ON UPDATE CASCADE ON DELETE SET NULL
            )
            """
        )
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_players_team ON players(teamCode)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_matches_status ON matches(status)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_matches_date ON matches(match_date)")
