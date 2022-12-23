account0_name = ""
account0_balance = 0
account0_password = ""
account1_name = ""
account1_balance = 0
account1_password = ""
nAccounts = 0


def new_account(account_number, name, balance, password):
    global account0_name, account0_balance, account0_password
    global account1_name, account1_balance, account1_password

    if account_number == 0:
        account0_name = name
        account0_balance = balance
        account0_password = password
    if account_number == 1:
        account1_name = name
        account1_balance = balance
        account1_password = password


def show():
    global account0_name, account0_balance, account0_password
    global account1_name, account1_balance, account1_password
    if account0_name != "":
        print("Show: ")
        print("        Name: ", account0_name)
        print("        Balance: ", account0_balance)
        print("        Password: ", account0_password)
        print()

    if account1_name != "":
        print("Show: ")
        print("        Name: ", account1_name)
        print("        Balance: ", account1_balance)
        print("        Password: ", account1_password)
        print()


def get_balance(account_number, password):
    global account0_name, account0_balance, account0_password
    global account1_name, account1_balance, account1_password
    if account_number == 0:
        if password != account0_password:
            print("Incorrect password")
            return None
        return account0_balance
    if account_number == 1:
        if password != account1_password:
            print("Incorrect password")
            return None
        return account1_balance

