import psycopg2
from config import load_config

def create_tables():
    """func that will create tables is db"""
    commands = (
    """
    CREATE TABLE PhoneTable
    (
    ID SERIAL PRIMARY KEY,
    FirstName CHARACTER VARYING(30),
    LastName CHARACTER VARYING(30),
    PhoneNumber CHARACTER(11)
    );
    """,
    )

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                #execute creating tables 
                for command in commands:
                    
                    cur.execute(command)
    except (psycopg2.DatabaseError,Exception) as error:
        print (error)
    

if __name__ == '__main__':
    create_tables()

