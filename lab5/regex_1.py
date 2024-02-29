import re

def Ex1Match(string)->(re.Match):
    """
  It is more right to using search instead of match
    """
    pattern = '^a(b*)$'
    return re.search(pattern,string)

UserInput = input("Input your string:\t")

result = "accepted" if Ex1Match(UserInput) else "not accepted"

print(result)