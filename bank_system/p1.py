class User:
	def __init__(self, name, age, password=123, balance=100):
		self.name = name
		self.age = age
		self.password = password
		self.balance = balance

	def login_data(self):
		count = 3
		while count > 0:
			self._name = input("Enter Your Name Please :")
			self._age = int(input("Enter Your Age Please :"))
			self._password = int(input("Enter Your Password Please :"))
			if self._password == self.password:
				return True
			else:
				count -= 1
				return False

	def Welcome_person(self):
		print(f"Hello Mr.{self._name}")
		print(f"The Age Eqoul :{self._age}")
		print(f"The Password is :{self._password}")


class Bank(User):
	def __init__(self, name, age, password, balance):
		super().__init__(name, age, password, balance)

	def choose(self):
		# choose your service
		self.variable_Choose = int(input("Enter a number one to deposit your money ,"
		"or enter a number two digit number withdraw your sun :"))
		if self.variable_Choose == 1:
			bank.deposit("File deposit")
		elif self.variable_Choose == 2:
			bank.withdraw("File withdraw")

	def deposit(self, name_file):
		# determine your deposit amount
		self.d = float(input("Welcome, Please enter the amount of deposit :"))
		self.balance = self.balance + self.d
		if self.balance < 100:
			raise Exception("you have to put 100 at least")
		with open(f"{name_file}.txt", "w") as file_deposit:
			self.content_deposit = file_deposit.write(f"The current amount has become in case of deposit :{self.balance}")

	def withdraw(self, name_file):
		# determine your withdraw amount
		self.w = float(input("Welcome, Please enter the quantity of drag : "))
		self.balance = self.balance - self.w

		with open(f"{name_file}.txt", "w") as file_withdraw:
			self.content_withdraw = \
				file_withdraw.write(
					f"The current amount has become in case of withdraw :{self.balance}")


if __name__ == "__main__":
	user = User("Alaa", 22)

	if user.login_data():
		# call person
		user.Welcome_person()
		bank = Bank("Alaa", 22, 123, 100)
		# call your service
		bank.choose()
	else:
		print("Failed")

