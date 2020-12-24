class Asking:
    def __init__(self, request=int(input("Choose number among 1 - 20\n"))):
        self.request = request

    def pick_number(self):
        ask_user = int(input("put on your number that you choosed number 5\n"))
        ask_user2 = int(input("multipy your number by 3\n"))
        ask_user3 = int(input("subtract your result by 15\n"))
        sub_result = (self.request + ask_user) * ask_user2 - ask_user3
        ask_user4 = int(input("now tell me the result of your calculation and I'll tell you the number you choiced.\n"))

        return ask_user4
        # while not True:
        #     ask_user4 = int(input("I think that you are forget the number you picked please\ntype the correct result of calc.\n")) 
        #     if sub_result == ask_user4:
        #         return ask_user4  

    def last_calc(self):
        result = self.pick_number() / 3        
        return result
            

ask = Asking()

print("you picked number: %d" % ask.last_calc())