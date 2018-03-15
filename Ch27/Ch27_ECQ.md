# Chapter 27 ECQ
1.
a. 	------------------------------------------
	|		BankAccount		 |
	|AccountHolderName: 	  String	 |
	|IBAN: 		    	  Integer	 |
	|----------------------------------------|
	|CreateNewAccount()			 |
	|SetAccountHolderName()			 |
	|GetAccountHolderName()			 |
	|GetIBAN()				 |
	------------------------------------------

b.


class BankAccount:

	def __init__(self):
		self.accountHolderName = ""
		self.IBAN = 0

	def create_new_account(self, name = get_account_holder_name(), num):
		self.accountHolderName = name
		self.IBAN = num

	def set_account_holder_name(self)
		self.accountHolderName = input("What's the account holder"s name?")

	def get_account_holder_name(self):
		return self.accountHolderName

	def get_IBAN(self)
		return self.IBAN

c.
i. 