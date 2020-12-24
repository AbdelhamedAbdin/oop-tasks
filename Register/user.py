import json


class User:

    def __init__(self, username, password, confirm_password):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.user_list = []

    def check_username(self, user_request):
        # username length
        if len(user_request) <= 2:
            raise Exception("username should be 3 characters at least")
        return user_request

        # unique username
        # while True:
        #     self.user_list.append(user_request)
        #     if user_request in self.user_list:
        #         raise Exception("username is already exists")
        #     return

    def check_password(self, password_request):
        # password length
        if len(password_request) <= 4:
            raise Exception("username should be 5 characters at least")
        # valid confirmation password
        if password_request and self.confirm_password and password_request != self.confirm_password:
            raise Exception("password and confirm password not same")
        return password_request
