import re
def CapitalsWithSpaces(str):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str)
#/1 /2 groups
InnerText = input()

print(CapitalsWithSpaces(InnerText))