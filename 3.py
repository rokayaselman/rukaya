Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Bankaccount:
    def __init__(self,account_num,account_holder):
        self.account_num=account_num
        self.account_holder=account_holder
        self.balance=0.0
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited:",(amount),"$")
        print("Current balance:",(self.balance),"$")
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance!")
        else:
            self.balance-=amount
            print("withdraw:",(amount),"$")
            print("Current balance:",(self.balance),"$")
    def get_balance (self):
        return self.balance
    def __str__(self):
        return  "account holder:",(self.account_holder),"balance:",(self.balance),"$"
class SavingsAccaount(Bankaccount):
    def __init__(self,account_num,account_holder,interest_rate):
        super().__init__(account_num,account_holder)
        self.interest_rate=interest_rate
    def apply_interest(self):
        interest=self.balance*(self.interest_rate/100)
        self.balance+=interest
        print("interest:",(interest),"$")
        print("New balance:",(self.balance),"$")
    def __str__(self):
        return "Account Holder:",(self.account_holder),"Balance",(self.balance),"Interest Rate",(self.interest_rate)
    #----
account=Bankaccount("2861","rukai")
account.deposite(1000)
account.withdraw(500)
print(account)
savings=SavingsAccaount("2851","rukaii",35)
savings.deposit(1000)
savings.apply_interest()
print(savings)
