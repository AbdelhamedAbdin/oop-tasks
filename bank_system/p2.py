class User(object):
	def __init__(self, name, age, password, balance):
		self.name = name
		self.age = age
		self.password = 123
		self.balance = 100

	def Login_data(self):
		count = 3
		while count != 0:
			self.na_me = input("Enter Your Name Please :")
			self.a_ge = int(input("Enter Your Age Please :"))
			self.pass_word = int(input("Enter Your Password Please :"))
			if self.pass_word == self.password:
				return True
			else:
				count -= 1
				return False

	def Welcome_person(self):
		print(f"Hello Mr.{self.na_me}")
		print(f"The Age Eqoul :{self.a_ge}")
		print(f"The Password is :{self.pass_word}")


class Bank(User):
	def __init__(self, name, age, password, balance):
		self.name = name
		self.age = age
		self.password = 123
		self.balance = 100
		super().__init__(name, age, password, balance)

	def choose(self):
		self.variable_Choose = int(input("Enter a number one to deposit you money ,"
		"or enter a number two digit number withdraw your sun :"))
		if self.variable_Choose == 1:
			bank.deposit("File deposit")
		elif self.variable_Choose == 2:
			bank.withdraw("File withdraw")

	def deposit(self, name_file):
		self.d = float(input("Welcome,Please enter the amount of deposit :"))
		self.balance = self.balance + self.d
		with open(f"{name_file}.txt", "w") as file_deposit:
			self.content_deposit = file_deposit.write(
			f"The current amount has become in case of deposit :{self.balance}")

	def withdraw(self, name_file):
		self.w = float(input("Welcome,Please enter the quantity of drag :{self.balance}"))
		self.balance = self.balance - self.w
		with open(f"{name_file}.txt", "w") as file_wthdraw:
			self.content_withdraw = file_wthdraw.write(
			f"The current amount has become in case of withdraw :{self.balance}")


if __name__ == "__main__":
	user = User("Alaa", 22, 123, 100)
	if user.Login_data() == True:
		user.Welcome_person()
		bank = Bank("Alaa", 22, 123, 100)
		bank.choose()
	else:
		print("Failed")