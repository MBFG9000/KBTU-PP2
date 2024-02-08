class Useless:
    def __init__(self):
        self.string=''
    def getString(self):
        self.string=input()
    def printString(self):
        if self.string=='':
            print("You do not entered string")
        else:
            print(self.string.upper())

a = Useless()

a.getString()

a.printString()

