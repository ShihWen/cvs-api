import psycopg2
from config import config


def connect():
    """Connect to the PorstgreSQL database server"""
    conn = None
    try:
        params = config()

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        print('PostgresQL database version:')
        #cur.execute('SELECT version()')
        cur.execute('''SELECT extract_date
                       , store_name
                       , type
                       , city
                       , district
                       , address
                       , longitude
                       , latitude
                       , services
                FROM cnvnt_str_fm LIMIT 10''')

        db_content = cur.fetchone()
        print(db_content)
        # print([d[0].strftime('%Y-%m-%d') for d in db_content])

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()
