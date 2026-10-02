from django.db import connection

from apps.matches.entities.match_entity import MatchEntity
from apps.matches.repositories.interfaces import MatchRepository


class MatchRepositoryImpl(MatchRepository):
    def _map(self, r) -> MatchEntity:
        return MatchEntity(
            match_id=r[0],
            team1_code=r[1] or '',
            team2_code=r[2] or '',
            venue=r[3] or '',
            match_date=str(r[4] or ''),
            match_time=str(r[5] or ''),
            status=r[6] or '',
            winner_code=r[7] or '',
            team1_score=r[8] or '',
            team2_score=r[9] or '',
            player_of_match=r[10] or '',
        )

    def list_all(self) -> list[MatchEntity]:
        sql = 'SELECT match_id, team1_code, team2_code, venue, match_date, match_time, status, winner_code, team1_score, team2_score, player_of_match FROM matches ORDER BY match_date DESC, match_id DESC'
        with connection.cursor() as c:
            c.execute(sql)
            return [self._map(r) for r in c.fetchall()]

    def get_by_id(self, match_id: int) -> MatchEntity | None:
        sql = 'SELECT match_id, team1_code, team2_code, venue, match_date, match_time, status, winner_code, team1_score, team2_score, player_of_match FROM matches WHERE match_id=%s'
        with connection.cursor() as c:
            c.execute(sql, [match_id])
            r = c.fetchone()
        return self._map(r) if r else None

    def add(self, match: MatchEntity) -> bool:
        sql = '''
        INSERT INTO matches (match_id, match_date, match_time, team1_code, team2_code, venue, status, winner_code, team1_score, team2_score, player_of_match)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        with connection.cursor() as c:
            return c.execute(sql, [
                match.match_id, match.match_date or None, match.match_time or None,
                match.team1_code or None, match.team2_code or None, match.venue or None,
                match.status, match.winner_code or None, match.team1_score or None, match.team2_score or None,
                match.player_of_match or None,
            ]) > 0

    def update(self, match: MatchEntity) -> bool:
        sql = '''
        UPDATE matches
        SET match_date=%s, match_time=%s, team1_code=%s, team2_code=%s, venue=%s, status=%s,
            winner_code=%s, team1_score=%s, team2_score=%s, player_of_match=%s
        WHERE match_id=%s
        '''
        with connection.cursor() as c:
            return c.execute(sql, [
                match.match_date or None, match.match_time or None, match.team1_code or None, match.team2_code or None,
                match.venue or None, match.status, match.winner_code or None, match.team1_score or None,
                match.team2_score or None, match.player_of_match or None, match.match_id,
            ]) > 0

    def delete(self, match_id: int) -> bool:
        with connection.cursor() as c:
            return c.execute('DELETE FROM matches WHERE match_id=%s', [match_id]) > 0
