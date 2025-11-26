
class BankAccount():
 
    def __init__(self, balance):
        self.balance = balance
    
    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw_money(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")


class SavingsAccount(BankAccount):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw_money(self, amount):
        if amount > 0:
            if self.balance - amount >= self.min_balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                raise ValueError(f"Cannot withdraw ${amount}. Balance would fall below minimum balance of ${self.min_balance}")
        else:
            print("Withdrawal amount must be positive")

if __name__ == "__main__":
    print("=== Regular Bank Account ===")
    account1 = BankAccount(1000)
    account1.deposit_money(500)
    account1.withdraw_money(200)
    
    print("\n=== Savings Account ===")
    savings = SavingsAccount(balance=1000, min_balance=500)
    savings.deposit_money(300)
    savings.withdraw_money(400)  
    
    print("\nTrying to withdraw a lot:")
    try:
        savings.withdraw_money(500)  
    except ValueError as e:
        print(f"Error: {e}")
        
    

