import psycopg2
from config import load_config


def DeleteByID(ID):
    config = load_config()
    rows_deleted = 0

    sql = "DELETE FROM PhoneTable WHERE ID = %s"
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (ID,))
                rows_deleted = cur.rowcount

            conn.commit()
    except (psycopg2.DatabaseError,Exception) as error:
        print(error)
    finally:
        return rows_deleted
    
if __name__ == '__main__':
    deleted_rows = DeleteByID(3)
    print('The number of deleted rows: ', deleted_rows)