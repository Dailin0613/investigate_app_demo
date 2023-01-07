from database.database import get_connection
from .entities.Project import Project


class ProjectModel:
    @classmethod
    def get_project(self):
        try:
            conn = get_connection()
            projects = []
            with conn.cursor() as cursor:
                cursor.execute('SELECT id, team_name, name, description, objective, problem, hypothesis FROM project')
                result = cursor.fetchall()

                for row in result:
                    project = Project(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    projects.append(project.to_json())

            conn.close()
            return projects

        except Exception as ex:
            raise ex

    @classmethod
    def add_project(self, project):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute('''INSERT INTO project (id, team_name, name, description, objective, problem, hypothesis)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                               (project.id, project.team_name, project.name, project.description,
                                project.objective, project.problem, project.hypothesis))
                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows

        except Exception as ex:
            raise ex

    @classmethod
    def delete_project(self, project):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM project WHERE id = %s', (project.id,))

                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows

        except Exception as ex:
            raise ex

    @classmethod
    def update_project(self, project):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute('''UPDATE project SET team_name = %s, name = %s, description = %s, objective = %s, 
                            problem = %s, hypothesis = %s WHERE id = %s''',
                               (project.team_name, project.name, project.description,
                                project.objective, project.problem, project.hypothesis, project.id))

                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows

        except Exception as ex:
            raise ex
