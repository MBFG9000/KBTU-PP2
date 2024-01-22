a=int(input())
b=int(input())

#23:03 m first program that do simple math with a and b

print("Addition of \t",a,"\t and \t",b,"\t is: \t",a+b,end=";\n")
print("Multiplication of\t",a," \t and\t",b,"\t is: \t",a*b,end=";\n")
print("Substraction of\t",a," \t and\t",b,"\t is: \t",a-b,end=";\n")
print("Division of \t",a," \t and\t",b,"\t is: \t",a/b,end=";\n")
print("\t",a,"\tin the power of\t",b,"\t is: \t",a**b,end=";\n")
2

print("***Test is succesful***")

#if else training 23:14

choice = int(input("Try to guess number that i randomly picked:\t"))
guessNumber=42

if choice == guessNumber:
    print("Wow! You're right")
elif choice == 69:
    print("Not funny bro")
elif guessNumber-choice <= 10 and guessNumber-choice >= -10:
    print("You are pretty near")
else:
    print("Sorry bro.You are far asf")

print("***Test is succesful***")

#for and list training  23:42

ourGang=["Andrey","Mirkhat","Vladislav","Ilya","Tamerlan"]#sorry too lazy to write all of you love you so much guys
for member in ourGang:
    print(member,"Dick length\t",len(member)," meters")

print("***Test is succesful***")

for i in range(10):
    print(i,end=",")
print()
for i in range(4,10):
    print(i,end=",")
print()
for i in range(2,10,2):
    print(i,end=",")
print()
print("***Test is succesful***")

for i in range(len(ourGang)):
    print(i,ourGang[i])
print("***Test is succesful***")
#range is not list example:

print(max(range(10)))
print(sum(range(4)))
print("***Test is succesful***")
#break continue etc
#find perfect squre between 1 and 100

for i in range(100):
    for j in range (2,i):
        if  j*j==i:
            print(i,end=',')
            break
        
