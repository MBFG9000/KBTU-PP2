"""
Класс — шаблон, с помощью которого удобно описывать однотипные объекты. 
В классе соержатся свойства, правила создания и поведение объекта.

    Объект — экземпляр, созданный на основе шаблона.

    Атрибут — поле, хранящее значение. Содержит свойства объекта.

    Метод — функция, связанная с классом. Описывает поведение или действия объекта.
"""

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

print("#"*20)

def myFunction() :
  return True

print(myFunction())

print("#"*20)

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

print("#"*20)

x = 200
print(isinstance(x, int)) #just check is x is int

