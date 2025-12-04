class BankAccount():
 
    def __init__(self, balance):
        self.balance = balance
    
    def deposit_money(self, amount):
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw_money(self, amount):
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"


class SavingsAccount(BankAccount):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw_money(self, amount):
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if self.balance - amount < self.min_balance:
            raise ValueError(f"Cannot withdraw ${amount}. Balance would fall below minimum balance of ${self.min_balance}")
        
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"


if __name__ == "__main__":
    print("=== Regular Bank Account ===")
    account1 = BankAccount(1000)
    
    try:
        message = account1.deposit_money(500)
        print(message)
        
        message = account1.withdraw_money(200)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== Savings Account ===")
    savings = SavingsAccount(balance=1000, min_balance=500)
    
    try:
        message = savings.deposit_money(300)
        print(message)
        
        message = savings.withdraw_money(400)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== Testing Invalid Operations ===")
    
    print("Trying to deposit negative amount:")
    try:
        savings.deposit_money(-100)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nTrying to withdraw negative amount:")
    try:
        savings.withdraw_money(-50)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nTrying to withdraw too much:")
    try:
        savings.withdraw_money(500)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nTrying to withdraw from regular account (insufficient funds):")
    try:
        account1.withdraw_money(10000)
    except ValueError as e:
        print(f"Error: {e}")