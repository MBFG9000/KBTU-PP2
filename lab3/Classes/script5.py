"""
def FindPrime(v):
    for i in range(2,v)
        if v%i==0:
            return False
    return True 



    x=lambda v: all([v%i for i in range(2, int(v**0.5) + 1)]) and num > 1
    all-return true when whole list true,true when list empty
    0-falsy value
    sqrt from discrete math concept number theory 
    Dzhankieva apai van love 
"""
listofnum=list(range(120))

PrimeSort=filter(lambda v: all([v%i for i in range(2, int(v**0.5) + 1)]) and v > 1,listofnum)
#The result is always filter object so I will need to convert it to list using list()
listofnum=list(PrimeSort)
print(listofnum)