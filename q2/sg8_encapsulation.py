class BankAccount:  #creates the BankAccount class
    def __init__(self, account_number: int, balance: float):  #constructor to initialize attributes
        self.__account_number = 0  #initializes private account number 
        self.__balance = 0  #initializes private balance 
        self.set_account_number(account_number)  #validates and sets the account number 
        self.set_balance(balance)  #validates and sets the balance

    def set_account_number(self, account_number):  #setter function for account number
        if account_number > 0:  #checks if the account number is greater than zero
            self.__account_number = account_number  #updates the private attribute if valid

    def get_account_number(self):  #getter function for account number
        return self.__account_number  #returns the private account number value

    def set_balance(self, balance):  #setter function for balance
        if balance < 0:  #checks if the balance being set is negative
            print("The balance must not be a negative number.") #prints error message if it's negative
        else:  #runs if the balance is valid
            self.__balance = balance  #updates the private balance attribute

    def get_balance(self):  #getter function for balance
        return self.__balance  #returns the current balance value


# Testing the class
a1 = BankAccount(12345, 1000)  #creates a BankAccount object
print("Account 1")  #prints a title label
print("Account Number:", a1.get_account_number())  #fetches and prints the account number
print("Balance:", a1.get_balance())  #fetches and prints the initial balance

print()  #prints an empty line
print("Update Balance to -100")  #prints for the next test case
a1.set_balance(-100)  #update the balance to a negative value
print("Account Number:", a1.get_account_number())  #prints account number to verify it stayed the same
print("Balance:", a1.get_balance())  #prints balance to verify it didn't change
