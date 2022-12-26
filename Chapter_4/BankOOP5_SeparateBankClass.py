from Account import *


class Bank:
    def __init__(self) -> None:
        self.account_dict = {}
        self.next_account_number = 0

    def create_account(self, the_name, the_starting_amount, the_password):
        o_account = Account(the_name, the_starting_amount, the_password)
        new_account_number = self.next_account_number
        self.account_dict[new_account_number] = o_account
        self.next_account_number += 1
        return new_account_number

    def open_account(self):
        print("*** Open Account ***")
        user_name = input("What is the name for the new user account? ")
        user_starting_amount = input("What is the starting balance for this account? ")
        user_starting_amount = int(user_starting_amount)
        user_password = input("What is the password you want to use for this account? ")
        user_account_number = self.create_account(
            user_name, user_starting_amount, user_password
        )
        print("Your new account number is: ", user_account_number)
        print()

    def close_account(self):
        print("*** Close Account ***")
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_account_password = input("Please enter the password: ")
        o_account = self.account_dict[user_account_number]
        the_balance = o_account.get_balance(user_account_password)
        if the_balance is not None:
            print(
                "Your had ",
                the_balance,
                " in your account, which is being returned to you.",
            )
            del self.account_dict[user_account_number]
            print("Your account is now closed.")

    def balance(self):
        print("*** Get Balance ***")
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_account_password = input("Please enter the password: ")
        o_account = self.account_dict[user_account_number]
        the_balance = o_account.get_balance(user_account_password)
        if the_balance is not None:
            print("Your balance is: ", the_balance)

    def deposit(self):
        print("*** Deposit ***")
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_deposit_amount = input("Please enter amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_account_password = input("Please enter the password: ")
        o_account = self.account_dict[user_account_number]
        the_balance = o_account.deposit(user_deposit_amount, user_account_password)
        if the_balance is not None:
            print("Your new balance is: ", the_balance)

    def show(self):
        print("Show")
        for user_account_number in self.account_dict:
            o_account = self.account_dict[user_account_number]
            print("     Account number: ", user_account_number)
            o_account.show()

    def withdraw(self):
        print("*** Withdraw ***")
        user_account_number = input("Please enter your account number: ")
        user_account_number = int(user_account_number)
        user_withdraw_amount = input("Please enter amount to withdraw: ")
        user_withdraw_amount = int(user_withdraw_amount)
        user_account_password = input("Please enter the password: ")
        o_account = self.account_dict[user_account_number]
        the_balance = o_account.withdraw(user_withdraw_amount, user_account_password)
        if the_balance is not None:
            print("Your new balance is: ", the_balance)
