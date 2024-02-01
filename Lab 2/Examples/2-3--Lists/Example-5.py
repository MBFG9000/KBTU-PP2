thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#just removing element

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#just removing by index loool

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#if you are lazy programmer that not writed index it just delete last

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#same as first

thislist = ["apple", "banana", "cherry"]
del thislist

#full list delete

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#same thing as previous
