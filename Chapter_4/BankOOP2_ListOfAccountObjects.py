from Account import *

account_list = []

o_account_1 = Account('Zoan', 1000, 'zh')
account_list.append(o_account_1)

o_account_2 = Account('Kanojo', 1500, 'zh')
account_list.append(o_account_2)

account_list[0].show()
account_list[1].show()

print('Calling methods of two accounts ...')
account_list[0].deposit(100, 'zh')
account_list[1].withdraw(100, 'zh')
account_list[1].deposit(100, 'zh')

account_list[0].show()
account_list[1].show()

print()
user_name = input('What is the name for the new user account? ')
user_balance = input('What is the starting balance for this account? ')
user_balance = int(user_balance)
user_password = input('What is the password you want to use for this account? ')
o_new_account = Account(user_name, user_balance, user_password)
account_list.append(o_new_account)

print('Created new account, acountnumber is 2')
account_list[2].show()

account_list[2].deposit(100, 'zh')
user_balance = account_list[2].get_balance('zh')
print()
print('After depositing 100, the user"s balance is: ', user_balance)