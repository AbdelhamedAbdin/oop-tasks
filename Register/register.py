import json 
from user import User


class Register(User):
	def __init__(self, username, password, confirm_password):
		super().__init__(username, password, confirm_password)
		self.is_valid = False

	# check if user is Valid
	def validation_user(self):
		register = Register(
			self.check_username(self.username.lower()),
			self.check_password(self.password),
			self.confirm_password
			)

		if register:
			self.is_valid = True
		else:
			raise Exception("Invalid Form")

	# save data if it is valid
	def save(self, **kwargs):
		if self.is_valid:
			self.username_arr = []
			self.username_arr.append(reg.check_username(self.username.lower()))
			kwargs['user'] = {
				"username": self.username_arr,
				"password": reg.check_password(self.password),
				"confirm_password": reg.confirm_password
			}

			json.dump(kwargs, open("user_table.json", "w+"), indent=4)
			return "You have registered successfully"
		else:
			raise Exception("didn't save")


if __name__ == "__main__":
	reg = Register("ALI", "medoabdin", "medoabdin")
	if reg.validation_user():
		reg.save()
	print(reg.save())
