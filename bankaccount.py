class BankAccount: "Bank of Plumbob"
    interest_rate = 6
    balance= 100
# don't forget to add some default values for these parameters!
    def __init__(self, name, int_rate, balance): 
        self.name: name
        self.int_rate= int_rate
        self.balance= balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print (f"Name:{self.name} Balance:{self.balance}")
        return self
    
    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        print(self.display_account_info())
        return self
        

Magoogalu = BankAccount("Magoogalu", 3.3, 202)
Maoguai= BankAccount("Maoguai", 2.17,123 )

Magoogalu.deposit(2).deposit(11).deposit(23).withdraw(5).yield_interest().display_account_info()   
Maoguai.deposit(1000).deposit(500).withdraw(6).withdraw(25).withdraw(86).withdraw(95).yield_interest().display_account_info()