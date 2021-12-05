"""Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank."""

class bankAccount:
    def __init__(self,acc_number,name,type_of_account,balance):
        self.acc_number=acc_number
        self.name=name
        self.type_of_account=type_of_account
        self.balance=balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance

    def withdraw(self,amount):
        self.balance=self.balance-amount
        return self.balance
    def currentbalance(self):
        return self.balance

if __name__=="__main__":
    b1=bankAccount("12345","Rahul","Savings",10000)
    print("Current Balance",b1.deposit(100))
    print("Current Balance",b1.withdraw(200))
    print("Current Balance",b1.currentbalance())



