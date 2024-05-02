import psycopg2
from config import load_config


def update_member(ID,**kwargs):
    """ Update member Lastname or First or PhoneNumber based on the id """
    
    set_params = ','.join([f"{key} = %s" for key in kwargs.keys()])

    # разделяет через запятую и добавляет значения для функции SET

    sql = f""" UPDATE PhoneTable
                SET {set_params}
                WHERE ID = %s"""
    
    
    config = load_config()
    
    values = list(kwargs.values()) + [ID]
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, values)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        pass

#ID , FirstName, LastName, Phonenumber
if __name__ == '__main__':
    update_member(1, LastName = 'Gavno', PhoneNumber = '87074523264')