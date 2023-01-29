import psycopg2 as dbconn

# connect to the PostgreSQL server
def connect(database, user, password, host, port):
    
    conn = dbconn.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port)

    cursor = conn.cursor()
    return conn, cursor

