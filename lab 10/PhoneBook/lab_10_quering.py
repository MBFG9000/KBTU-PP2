import psycopg2
from config import load_config

def getmembers():
    """ Retrieve data from the phonetable """
    config  = load_config()

    choicelist = ['FirstName', 'LastName', 'PhoneNumber']

    print("Which columns select? Write indexes separated by commas")
    for i in range(1,len(choicelist)+1):
        print(i,f". {choicelist[i-1]}")

    selectchoice = input().split(',')

    selected = []
    for index in selectchoice:
        selected.append (choicelist[int(index)-1])


    stringforselect = ",".join(selected)

    print(stringforselect)

    print("Which column choose to order? Write index")
    for i in range(1,len(choicelist)+1):
        print(i,f". {choicelist[i-1]}")

    index = int(input())


    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT ID,{stringforselect} FROM PhoneTable ORDER BY {choicelist[index-1]}")
                print("The number of parts: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    getmembers() 