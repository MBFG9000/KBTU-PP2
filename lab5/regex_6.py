import re

def ReplaceColon(word):
    return re.sub('[ ,.]',':',word)#re.sub(pattern, repl, string, count=0, flags=0) -> str

UserInput = input()

print(ReplaceColon(UserInput))