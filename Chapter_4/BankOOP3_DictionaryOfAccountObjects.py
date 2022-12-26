from Account import *

account_dict = {}
next_account_number = 0

#! Create two accounts
o_account = Account("Zoan", 1000, "zh")
zoan_account_number = next_account_number
account_dict[zoan_account_number] = o_account
print("Account number for Zoan is: ", zoan_account_number)
next_account_number += 1

o_account = Account("Hy", 1000, "zh")
hy_account_number = next_account_number
account_dict[hy_account_number] = o_account
print("Account number for Hy is: ", hy_account_number)
next_account_number += 1

account_dict[zoan_account_number].show()
account_dict[hy_account_number].show()

print("Calling methods of the two accounts ...")
account_dict[zoan_account_number].deposit(100, "zh")
account_dict[hy_account_number].deposit(100, "zh")
account_dict[hy_account_number].withdraw(100, "zh")

#! show the accounts
account_dict[zoan_account_number].show()
account_dict[hy_account_number].show()

#! Create another account with information from the user
print()
user_name = input("What is the name for the new user account? ")
user_balance = input("What is the starting balance for this account? ")
user_balance = int(user_balance)
user_password = input("What is the password you want to use for this account? ")
o_account = Account(user_name, user_balance, user_password)
new_account_number = next_account_number
account_dict[next_account_number] = o_account
next_account_number += 1

account_dict[new_account_number].show()

#! Let's deposit 100 into the new account
account_dict[new_account_number].deposit(100, "zh")
user_balance = account_dict[new_account_number].get_balance("zh")
print()
print("After depositing 100, the user's balance is: ", user_balance)

account_dict[new_account_number].show()
