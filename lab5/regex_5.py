import re

def CheckWord(word):
    pattern = r'^a.*b$'
    return "accepted" if re.findall(pattern,word) else "not accepted"

UserInput = input()

print(CheckWord(UserInput))