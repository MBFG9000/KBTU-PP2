thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#append element to end

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#task:make your face serious and talk like you are pro
#also will be work(dont forget to say that you read it in documentation)

thislist = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "cherry",*tropical]


print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)