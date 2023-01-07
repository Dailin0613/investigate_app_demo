from psycopg2 import connect, DatabaseError

host = 'localhost'
port = 5432
user = 'postgres'
password = 'root'
database = 'investigation'


def get_connection():
    try:
        conn = connect(
            host=host, port=port, user=user, password=password, database=database
        )
        return conn
    except DatabaseError as ex:
        raise ex
