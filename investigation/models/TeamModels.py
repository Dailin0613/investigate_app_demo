from database.database import get_connection
from .entities.Team import Team


class TeamModel:
    @classmethod
    def get_team(self):
        try:
            conn = get_connection()
            teams = []
            with conn.cursor() as cursor:
                cursor.execute('SELECT id, name, objective, description, goal FROM team')
                result = cursor.fetchall()

                for row in result:
                    team = Team(row[0], row[1], row[2], row[3], row[4])
                    teams.append(team.to_json())

            conn.close()
            return teams

        except Exception as ex:
            raise ex

    @classmethod
    def add_team(self, team):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute('''INSERT INTO team (id, name, objective, description, goal)
                                VALUES (%s, %s, %s, %s, %s)''',
                               (team.id, team.name, team.objective, team.description, team.goal))
                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows

        except Exception as ex:
            raise ex

    @classmethod
    def delete_team(self, team):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM team WHERE id = %s', (team.id,))

                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows

        except Exception as ex:
            raise ex

    @classmethod
    def update_team(self, team):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute('''UPDATE team SET name = %s, objective = %s, description = %s, goal = %s WHERE id = 
                              %s''', (team.name, team.objective, team.description, team.goal, team.id))

                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows

        except Exception as ex:
            raise ex
