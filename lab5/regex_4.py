import re

def CheckWord(word):
    pattern = r'^[A-Z][a-z]+$'
    return "accepted" if re.findall(pattern,word) else "not accepted"

UserInput = input()

print(CheckWord(UserInput))