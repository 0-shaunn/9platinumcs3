class BankAccount: #Creating the Class

    def __init__(self, account_number: int, balance: float):
        self.__account_number = 0 #Private Attributes
        self.__balance = 0
        self.set_account_number(account_number) #Public Methods
        self.set_balance(balance)

  #Setter for Account Number
    def set_account_number(self, account_number):
        if account_number > 0:
            self.__account_number = account_number

  #Getter for Account Number
    def get_account_number(self):
        return self.__account_number

  #Setter for Balance
    def set_balance(self, balance):
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = balance

  #Getter for Balance
    def get_balance(self):
        return self.__balance


# Testing the class
a1 = BankAccount(12345, 1000)
print("Account 1")
print("Account Number:", a1.get_account_number())
print("Balance:", a1.get_balance())

print()
print("Update Balance to -100")
a1.set_balance(-100)
print("Account Number:", a1.get_account_number())
print("Balance:", a1.get_balance())
