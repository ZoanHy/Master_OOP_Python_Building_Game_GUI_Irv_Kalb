from Account import *

account_dict = {}
next_account_number = 0

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
        print("*** Get Balance ***")
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_account_password = input("Please enter the password: ")
        o_account = account_dict[user_account_number]
        the_balance = o_account.get_balance(user_account_password)
        if the_balance is not None:
            print("Your balance is: ", the_balance)
    elif action == "d":
        print("*** Deposit ***")
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_deposit_amount = input("Please enter amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_account_password = input("Please enter the password: ")
        o_account = account_dict[user_account_number]
        the_balance = o_account.deposit(user_deposit_amount, user_account_password)
        if the_balance is not None:
            print("Your new balance is: ", the_balance)
    elif action == "o":
        print("*** Open Account ***")
        user_name = input("What is the name for the new user account? ")
        user_starting_amount = input("What is the starting balance for this account? ")
        user_starting_amount = int(user_starting_amount)
        user_password = input("What is the password you want to use for this account? ")
        o_account = Account(user_name, user_starting_amount, user_password)
        account_dict[next_account_number] = o_account
        print("Your new account number is: ", next_account_number)
        next_account_number += 1
        print()
    elif action == "s":
        print("Show")
        for user_account_number in account_dict:
            o_account = account_dict[user_account_number]
            print("     Account number: ", user_account_number)
            o_account.show()
    elif action == "q":
        break
    elif action == "w":
        print("*** Withdraw ***")
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_withdraw_amount = input("Please enter amount to withdraw: ")
        user_withdraw_amount = int(user_withdraw_amount)
        user_account_password = input("Please enter the password: ")
        o_account = account_dict[user_account_number]        
        the_balance = o_account.withdraw(user_withdraw_amount, user_account_password)
        if the_balance is not None:
            print("Your new balance is: ", the_balance)
    else:
        print("Sorry, that was not a valid action. Please try again.")
print("Done")
