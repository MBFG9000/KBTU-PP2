thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)  

#If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#random remove

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)  