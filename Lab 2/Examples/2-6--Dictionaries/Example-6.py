for x in thisdict:
  print(x)



for x in thisdict:
  print(thisdict[x])

#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)


#You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)


#loop both
for x, y in thisdict.items():
  print(x, y)