#1
ConvertToOun=lambda g: 28.3495231 * g
#2
ConvertToC=lambda f: (5 / 9) * (f - 32)
#3
def ProblemSolve(heads,legs): 
    """
    chicken * 2 + rabbit * 4 = legs
    x=chicken   rabbit=heads-x

    x*2+(heads-x)*4 = legs
    2x + 4heads - 4x = legs
    -2x = legs -4heads
    x = -0,5*legs + 2*heads

    """
    chicken = -0.5*legs + 2*heads
    rabbit = heads - chicken
    return f"Chikens:{chicken} and Rabbits:{rabbit}"
#4
def filter_prime(_list:list)->(list):  
    ReturnList=[]
    for member in _list:
        app= True if member > 1 else False
        for i in range(2,int(member**0.5+1)):
            if member%i==0:
                app=False
                break
        if app:
            ReturnList.append(member)     
    return ReturnList
#5




"""
a=list("dcba")
a.sort()
print(str(a))

print(filter_prime(list(range(100))))


print(ProblemSolve(35,94))

print(ConvertToOun(2))

print(ConvertToC(80))

"""