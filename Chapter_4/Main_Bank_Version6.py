from BankOOP6_UsingExceptions import Account, AbortTransaction


class Bank:
    def __init__(self, hours, address, phone) -> None:
        self.account_dict = {}
        self.next_account_number = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def ask_for_valid_account_number(self):
        account_number = input("What is your account number? ")
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction("The account number must be an integer")
        if account_number not in self.account_dict:
            raise AbortTransaction("There is no account " + str(account_number))
        return account_number

    def get_user_account(self):
        account_number = self.ask_for_valid_account_number()
        o_account = self.account_dict[account_number]
        o_account.check_password_match()
        return o_account

    def deposit(self):
        print("*** Deposit ***")
        o_account = self.get_user_account()
        deposit_amount = input("Please enter amount to deposit: ")
        the_balance = o_account.deposit(deposit_amount)
        print("Deposited: ", deposit_amount)
        print("Your new balance is: ", the_balance)

    def withdraw(self):
        print("*** Withdraw ***")
        o_account = self.get_user_account()
        withdraw_amount = input("Please enter amount to deposit: ")
        the_balance = o_account.withdraw(withdraw_amount)
        print("Withdrew: ", withdraw_amount)
        print("Your new balance is: ", the_balance)

    def get_info(self):
        print("Hours:", self.hours)
        print("Address:", self.address)
        print("Phone:", self.phone)
        print("We currently have", len(self.account_dict), "account(s) open.")

    def show(self):
        print("*** Show ***")
        print("(This would typically require an admin password)")
        for user_account_number in self.account_dict:
            o_account = self.account_dict[user_account_number]
            print("     Account number: ", user_account_number)
            o_account.show()
            print()

