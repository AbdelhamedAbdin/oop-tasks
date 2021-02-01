import json
import random

text = "Hello world"

x = text.split()

for answer in x:
    if answer == "":
        answer = "-"
    else:
        answer = answer

    print(answer)

