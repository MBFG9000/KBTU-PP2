class BankAccount:
    def __init__(self,FullName):
        self.name=FullName
        self.balance = 0
    def deposit(self):
        print(f"Hello, dear {self.name}.Your balance is {self.balance}$\nType the sum of your deposit :\t",end="")
        sum=int(input())
        if sum < 0:
            print("Sorry.It is not avaible")
        elif sum == 0:
            print("Sorry.It is not avaible")
        else:
            self.balance+=sum
    def withdraw(self):
        print(f"Hello, dear {self.name}.Your balance is {self.balance}$\nHow much do you want to withdraw from your account :\t",end="")
        sum=int(input())
        
        if sum > self.balance:
            print("Unfortunately, you don't have enough balance")
        else:
            self.balance-=sum
            print(f"Have a great day {self.name}. Your balance {self.balance}$ ")




a=BankAccount("Jordan Belford")
a.deposit()
a.withdraw()
print(a.balance)


