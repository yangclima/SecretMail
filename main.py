from encrypt import *
from inputProcessing import *
from userAdmin import userAdmin

userVariables = userAdmin.userContent.get("localVariables")
tempVariables = {}


while True:
    userInput = commandDetector(input(">> "), userVariables, tempVariables)
    result = ""

    match userInput[0]:
        case "encrypt":
            result = encrypt(userInput[1], getKey(userInput[2]))
            print(result)

        case "decrypt":
            result = decrypt(userInput[1], getKey(userInput[2]))
            print(result)

        case "setVariable":
            tempVariables.update({userInput[1]: userInput[2]})

        case _: 
            pass

