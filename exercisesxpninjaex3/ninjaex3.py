from random import randint
from random import choice
import string


lowletters = string.ascii_lowercase
uppletters = string.ascii_uppercase

passlength = int(input("Please enter password length, min 6 max 30 chars: "))

methodsused = []
password = []

def passwordcreator():
    password.clear()

    for x in range(passlength):
        picker = randint(0,3)

        if picker == 0:
            number = randint(0,9)
            password.append(str(number))
            methodsused.append(0)

        if picker == 1:
            lowletter = choice(lowletters)
            password.append(lowletter)
            methodsused.append(1)

        if picker == 2:
            uppletter = choice(uppletters)
            password.append(uppletter)
            methodsused.append(2)

        if picker == 3:
            specialchar = choice(string.punctuation)
            password.append(specialchar)
            methodsused.append(3)

taskcomplete = False

while taskcomplete == False:
    if (0 in methodsused) and (1 in methodsused) and (2 in methodsused) and (3 in methodsused):
        print("Your password:","".join(password))
        taskcomplete = True
    else:
        passwordcreator()

# at least 1 digit 0-9
# at least 1 lower case a-z
# at least 1 upper case A-Z
# at least 1 specila char

