from django.db import connection

from apps.players.entities.player_entity import PlayerEntity
from apps.players.repositories.interfaces import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    def _map_row(self, row) -> PlayerEntity:
        return PlayerEntity(
            jersey_number=row[0],
            player_name=row[1],
            age=row[2],
            role=row[3],
            nationality=row[4],
            team_code=row[5],
            image_path=row[6] or '',
        )

    def list_all(self) -> list[PlayerEntity]:
        with connection.cursor() as cursor:
            cursor.execute('SELECT jerseyNumber, playerName, age, role, nationality, teamCode, imagePath FROM players')
            return [self._map_row(r) for r in cursor.fetchall()]

    def list_by_team(self, team_code: str) -> list[PlayerEntity]:
        with connection.cursor() as cursor:
            cursor.execute('SELECT jerseyNumber, playerName, age, role, nationality, teamCode, imagePath FROM players WHERE teamCode=%s', [team_code])
            return [self._map_row(r) for r in cursor.fetchall()]

    def get_by_jersey(self, jersey_number: int, team_code: str) -> PlayerEntity | None:
        with connection.cursor() as cursor:
            cursor.execute('SELECT jerseyNumber, playerName, age, role, nationality, teamCode, imagePath FROM players WHERE jerseyNumber=%s AND teamCode=%s', [jersey_number, team_code])
            row = cursor.fetchone()
        return self._map_row(row) if row else None

    def add(self, player: PlayerEntity) -> bool:
        sql = 'INSERT INTO players (jerseyNumber, playerName, age, role, nationality, teamCode, imagePath) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        with connection.cursor() as cursor:
            return cursor.execute(sql, [player.jersey_number, player.player_name, player.age, player.role, player.nationality, player.team_code, player.image_path]) > 0

    def update(self, player: PlayerEntity) -> bool:
        sql = 'UPDATE players SET playerName=%s, age=%s, role=%s, nationality=%s, imagePath=%s WHERE jerseyNumber=%s AND teamCode=%s'
        with connection.cursor() as cursor:
            return cursor.execute(sql, [player.player_name, player.age, player.role, player.nationality, player.image_path, player.jersey_number, player.team_code]) > 0

    def delete(self, jersey_number: int, team_code: str) -> bool:
        with connection.cursor() as cursor:
            return cursor.execute('DELETE FROM players WHERE jerseyNumber=%s AND teamCode=%s', [jersey_number, team_code]) > 0
