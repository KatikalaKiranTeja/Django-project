from django.db import connection

from apps.teams.entities.team_entity import TeamEntity
from apps.teams.repositories.interfaces import TeamRepository


class TeamRepositoryImpl(TeamRepository):
    def list_all(self) -> list[TeamEntity]:
        sql = "SELECT teamCode, teamName, country, coachName, captainName, logoPath FROM teams"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
        return [
            TeamEntity(
                team_code=row[0],
                team_name=row[1],
                country=row[2],
                coach_name=row[3],
                captain_name=row[4],
                logo_path=row[5] or '',
            )
            for row in rows
        ]

    def get_by_code(self, team_code: str) -> TeamEntity | None:
        sql = "SELECT teamCode, teamName, country, coachName, captainName, logoPath FROM teams WHERE teamCode=%s"
        with connection.cursor() as cursor:
            cursor.execute(sql, [team_code])
            row = cursor.fetchone()
        if not row:
            return None
        return TeamEntity(
            team_code=row[0],
            team_name=row[1],
            country=row[2],
            coach_name=row[3],
            captain_name=row[4],
            logo_path=row[5] or '',
        )

    def exists(self, team_code: str) -> bool:
        sql = "SELECT 1 FROM teams WHERE teamCode=%s"
        with connection.cursor() as cursor:
            cursor.execute(sql, [team_code])
            return cursor.fetchone() is not None

    def add(self, team: TeamEntity) -> bool:
        sql = """
        INSERT INTO teams (teamCode, teamName, country, coachName, captainName, logoPath)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        with connection.cursor() as cursor:
            return cursor.execute(
                sql,
                [
                    team.team_code,
                    team.team_name,
                    team.country,
                    team.coach_name,
                    team.captain_name,
                    team.logo_path,
                ],
            ) > 0

    def update(self, team: TeamEntity) -> bool:
        sql = """
        UPDATE teams
        SET teamName=%s, country=%s, coachName=%s, captainName=%s, logoPath=%s
        WHERE teamCode=%s
        """
        with connection.cursor() as cursor:
            return cursor.execute(
                sql,
                [
                    team.team_name,
                    team.country,
                    team.coach_name,
                    team.captain_name,
                    team.logo_path,
                    team.team_code,
                ],
            ) > 0

    def delete(self, team_code: str) -> bool:
        sql = "DELETE FROM teams WHERE teamCode=%s"
        with connection.cursor() as cursor:
            return cursor.execute(sql, [team_code]) > 0
