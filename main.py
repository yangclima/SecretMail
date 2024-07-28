from encrypt import *
from inputProcessing import *
from userAdmin import userAdmin

tempVariables = {}


while True:
    userInput = commandDetector(
        input(f"{userAdmin.currentUser}>> "), 
        userAdmin.userContent.get("localVariables"), 
        tempVariables
        )

    match userInput["args"][0]:
        case "encrypt":
            result = encrypt(userInput["args"][1], getKey(userInput["args"][2]))
            print(result)

        case "decrypt":
            result = decrypt(userInput["args"][1], getKey(userInput["args"][2]))
            print(result)

        case "setVariable":
            if userInput.get("modifiers"):
                match userInput["modifiers"][0]:
                    case "-store":
                        userAdmin.storeVariable(userInput["args"][1], userInput["args"][2])
                    case _:
                        pass
            else:
                tempVariables.update({userInput["args"][1]: userInput["args"][2]})

        case "switchUser":
            userAdmin.switchUser()

        case _: 
            pass