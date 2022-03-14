class BankAccount: 
    bank_name= "Bank of Plumbob"

    def __init__(self, name, int_rate): #removed balance cuz account is deifned by a class 
        self.name= name
        self.int_rate= int_rate
        self.account= BankAccount(int_rate=0.02,balance=0)# this is the class

    def deposit(self, amount):
        self.account += amount #balance changed to account
        return self
    
    def withdraw(self, amount):
        self.account -= amount #balance changed to account
        return self
    
    def display_account_info(self):
        print (f"Name:{self.name} Balance:{self.account}") #balance changed to account
        return self
    
    def yield_interest(self):
        self.account += (self.account*self.int_rate) #balance shanged to account
        print(self.display_account_info())
        return self
        

Magoogalu = BankAccount("Magoogalu", 1.5)
Maoguai= BankAccount("Maoguai", 1.27)

Magoogalu.deposit(2).deposit(11).deposit(23).withdraw(5).yield_interest().display_account_info()   
Maoguai.deposit(1000).deposit(500).withdraw(6).withdraw(25).withdraw(86).withdraw(95).yield_interest().display_account_info()