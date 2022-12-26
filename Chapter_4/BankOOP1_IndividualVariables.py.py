from Account import *

o_account_1 = Account('Zoan', 1000, 'zh')
o_account_1.show()

o_account_2 = Account('Kanojo', 1500, 'zh')
o_account_2.show()

o_account_1.deposit(59, 'zh')
o_account_1.withdraw(59, 'zh')
o_account_2.deposit(19, 'zh')

o_account_1.show()
o_account_2.show()

user_name = input('What is the name for the new user account? ')
user_balance = input('What is the starting balance for this account? ')
user_balance = int(user_balance)
user_password = input('What is the password you want to use for this account? ')
o_new_account = Account(user_name, user_balance, user_password)

o_new_account.show()
o_new_account.deposit(100, user_password)
user_balance = o_new_account.get_balance(user_password)
print()
print("After depositing 100, the user's balance is: ", user_balance)
o_new_account.show()