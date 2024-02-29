import re

def Ex1Match(string)->(re.Match):
    pattern = r'^ab{2,3}$'
    return re.findall(pattern,string)

UserInput = input("Input your string:\t")

result = "accepted" if Ex1Match(UserInput) else "not accepted"

print(result)