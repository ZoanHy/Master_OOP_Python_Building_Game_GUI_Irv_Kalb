from BankOOP5_SeparateBankClass import *

o_bank = Bank()

# Main code
# Create two test accounts
joesAccountNumber = o_bank.create_account("Joe", 100, "JoesPassword")
print("Joe's account number is:", joesAccountNumber)
marysAccountNumber = o_bank.create_account("Mary", 12345, "MarysPassword")
print("Mary's account number is:", marysAccountNumber)

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press o to open a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")
    print()
    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0]  # grab the first letter
    print()
    if action == "b":
        o_bank.balance()
    elif action == "d":
        o_bank.deposit()
    elif action == "o":
        o_bank.open_account()
    elif action == "s":
        o_bank.show()
    elif action == "q":
        break
    elif action == "w":
        o_bank.withdraw()
    else:
        print("Sorry, that was not a valid action. Please try again.")
print("Done")
