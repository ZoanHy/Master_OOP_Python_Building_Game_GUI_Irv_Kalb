account_name = "zoan"
account_balance = 100
account_password = "zh"

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press w to make a withdrawal")
    print("Press s to show the account")
    print("Press q to quit")
    print()

    action = input("What do you want to do?")
    action = action.lower()  # ? force lowercase
    action = action[0]  # just use first letter
    print()

    if action == "b":
        print("Get Balance: ")
        user_password = input("Please enter the password: ")
        if user_password != account_password:
            print("Incorrect password")
        else:
            print("Your balance is: ", account_balance)
    elif action == "d":
        print("Deposit: ")
        user_deposit_amount = input("Please enter amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_password = input("Please enter the password: ")
        if user_deposit_amount < 0:
            print("You can't deposit a negative amount!")
        elif user_password != account_password:
            print("Incorrect password")
        else: #! OK
            account_balance = account_balance + user_deposit_amount
            print("Your new balance is: ", account_balance)
    elif action == "s":  # show
        print("Show: ")
        print("        Name: ", account_name)
        print("        Balance: ", account_balance)
        print("        Password: ", account_password)
    elif action == "q":
        break
    elif action == "w":
        print("Withdraw: ")
        user_withdraw_amount = input("Please enter the amount to withdraw: ")
        user_withdraw_amount = int(user_withdraw_amount)
        user_password = input("Please enter the password: ")

        if user_withdraw_amount < 0:
            print("You can't withdraw a negative amount")
        elif user_password != account_password:
            print("Incorrect password for this account")
        elif user_withdraw_amount > account_balance:
            print("You can't withdraw more than you have in your account")
        else:
            account_balance = account_balance - user_withdraw_amount
            print("Your new balance is: ", account_balance)
    print("Done")
    
