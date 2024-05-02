import psycopg2
from config import load_config
from lab_10_csvreader import ReadCSV
from lab_10_insertmembers import insert_member




def connect(config):
    """
        function that connect psycopg2 with database
    """
    try:
        with psycopg2.connect(**config) as conn:
            print("*"*40, "Succesfully connected to PostgreSQL server", "*"*40, sep = "\n")
            return conn
    except (psycopg2.DatabaseError,Exception) as error:
        print(error)

if __name__ == '__main__':
    config = load_config()
    conn = connect(config)


for member in ReadCSV('example.csv'):
    insert_member(**member)