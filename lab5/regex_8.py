import re

def CutAtUpper(InnerWord):
    return re.findall('[A-Z][^A-Z]*', InnerWord)
#^ here is negation
InnerText = input

print(CutAtUpper(InnerText))