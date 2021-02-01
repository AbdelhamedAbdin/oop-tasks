import json
import random
import time
import re


class Rules:
    '''
        this class explains the rules of game you can continue by clicking yes if you want
        to know what the game talking about.
    '''

    def choose_dict(self):
        prompt = str(input("do you want to start now?\nclick yes to continue or no to exit: "))

        if prompt == "yes":
            with open("film.json", "r") as fp:
                get_dict = json.load(fp)
                random_film = random.choice(get_dict["data"])
                return random_film
        elif prompt == "no":
            print("Game stopped")
            return
        else:
            raise Exception("you have to write just (yes/no) not any other word")

    def get_data(self):
        data_picked = self.choose_dict()
        if data_picked:
            tips = '''
                now the game will pick up the random dictionary that holds all information about the
                film that you have to know by writing the char you want so if it True: the char will
                be placed in the own place and if your choice is False: your choices will go down
                one by one depending on your answer if it was a mistake but remember 
                you have just 5 tries so, be careful until you don't be exposure to lose.
                so now, do you want to continue? (yes/no)
            '''
            tips = input(tips)

            if tips == "yes":
                print("genre is: %s" % data_picked["genre"])
                time.sleep(1)
                print("style is: %s" % data_picked["style"])
                time.sleep(1)
                print("count of letters are: %s" % data_picked["count_letters"])
                time.sleep(1)
                data = {
                    "count": data_picked["count_letters"],
                    "name": data_picked["name"]
                }
                return data

            elif tips == "no":
                print("the operation has stopped")
                return
            else:
                raise Exception("you have to write just yes or no not any other word")
        else:
            return

    def user_actions(self):
        obj = self.get_data()
        try_count = 5
        answers = []
        answer_count = 0
        ans = ""
        name_exact = obj.get("name")
        # char count in the name of film as a list
        while answer_count < len(name_exact):
            if name_exact[answer_count] == " ":
                answers.append(" ")
            else:
                answers.append("")
            answer_count += 1

        result = ""
        while True:
            print("character of film: %s" % answers)
            char_input = input("type char: ")
            # find the char matches
            if char_input.isalpha() or char_input.isdigit():
                if len(char_input) == 1:
                    match = re.finditer(char_input, name_exact)
                    index = [matchs.start() for matchs in match]
                    if char_input in name_exact:
                        for i in index:
                            answers[i] = char_input
                            print("you have %s attempts" % try_count)
                    else:
                        try_count -= 1
                        print("you have %s attempts" % try_count)
                else:
                    if char_input == name_exact:
                        print("excellent the film is: %s" % char_input)
                        break
                    else:
                        result = '''
                        ***********
                        Game Over
                        you lost all your attempts by one click
                        ***********
                        '''
                        print(result)
                        break
            else:
                raise Exception("input must be string of characters or digits")

            if obj:
                # stop the loop if the user lose his tries
                if try_count == 0:
                    print("Game Over")
                    break
                # stop the loop if the user was correct in his answer
                if "" not in answers:
                    result = result.join(answers)
                    print("excellent the film is: %s" % result)
                    break


if __name__ == "__main__":
    Rules().user_actions()
