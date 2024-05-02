import csv


def ReadCSV(file):
    memberlist =[]
    
    with open(file) as csvfile:
        data = csv.reader(csvfile)
        for row in data:
           memberlist.append(row)
    
    datakeys = memberlist[0]
    memberlist.pop(0)

    returning_maplsit = []

    for member in memberlist:
        map = {}
        for i in range (len(datakeys)):
            map[datakeys[i]] = member[i]
        returning_maplsit.append(map)                
    return returning_maplsit
            
if __name__ == '__main__':
    print(ReadCSV("example.csv"))


    