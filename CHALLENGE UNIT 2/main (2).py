class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than zero."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Amount must be greater than zero."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name} (Account #: {self.__account_number}): ${self.__account_balance}"


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("123456789", "John Doe", 1000.0)

    # Test deposit and withdrawal
    print(account.display_balance())  # Display initial balance
    print(account.deposit(500))  # Deposit $500
    print(account.withdraw(200))  # Withdraw $200
    print(account.display_balance())  # Display updated balance
    print(account.withdraw(2000))  # Attempt to withdraw $2000 (insufficient funds)
