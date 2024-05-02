from config import load_config
import psycopg2

def insert_member(FirstName, LastName, PhoneNumber):
    """Inserting new member in PhoneBook"""
    insert_cmd = """
        INSERT INTO Phonetable(FirstName,LastName,PhoneNumber)
        VALUES (%s,%s,%s) RETURNING ID
                 """
    
    ID = None
    
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_cmd, (FirstName, LastName, PhoneNumber))
                rows = cur.fetchone()
                if rows:
                    ID = rows[0]

                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

    finally:
        return ID
    

if __name__ == '__main__':
    insert_member("Temik", "legendov", "87775342345")