class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):

#All of the detail for a new back account.
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def calculating_interest_days(self, days):

#This will Calculate the interst after a certain amount of days.
        return self.amount * (self.interest_rate / 100) * (days / 365)

    def changed_interest_rate(self, new_interest_rate):

#Adjust the interest.
        self.interest_rate = new_interest_rate

    def deposit_amount(self, amount):

#Deposit amount.
        if amount > 0:
            self.amount += amount
        else:
            raise ValueError("Your deposit needs to be a positive number")

    def withdraw_amount(self, amount):

#Withdraw amount.
        if amount > 0 and amount <= self.amount:
            self.amount -= amount
        else:
            raise ValueError("Can not withdrawal this amount")

    def current_balance_amount(self):


        return self.amount

    
    def __str__(self):

#Return a string of account details.
        return f"Account Name: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.amount:.2f}\nInterest Rate: {self.interest_rate}%"


#Test Function
def test():
    #Test the functionality of the BankAcct class.
    account = BankAcct("Evon Kachline", "594228598", 52982.0, 10.0)
    print(account)

#Adjust interest rate
    account.changed_interest_rate(8.0)
    print("\nAdjusting The Interest Rate:")
    print(account)

#Deposit money
    account.deposit_amount(870.0)
    print("\nAmount After Deposit:")
    print(account)

#Withdraw money
    account.withdraw_amount(1050.0)
    print("\nAmount After Withdrawal:")
    print(account)

#Check balance
    balance = account.current_balance_amount()
    print(f"\nThe Current Balance: ${balance:.2f}")

#Calculate interest for set of days
    interest = account.calculating_interest_days(15)
    print(f"Interest for 15 days: ${interest:.2f}")



test()
