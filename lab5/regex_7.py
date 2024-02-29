import re
def SnakeToCamel(WordInSnake):
    ListOfWords = WordInSnake.split('_')
    WordInCamel = ''
    for member in ListOfWords:
        member = member[0].upper() + member[1:len(member)]
        WordInCamel+=member
    return WordInCamel

UserInput = input()

print(SnakeToCamel(UserInput))