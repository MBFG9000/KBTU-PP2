import re 

def Is_snake_case(text):
    pattern = r'^([a-z]+_)+[a-z]+$'
    return re.findall(pattern,text)

InnerString = input()

result = "accepted" if Is_snake_case(InnerString) else "not accapted" 

print(result)