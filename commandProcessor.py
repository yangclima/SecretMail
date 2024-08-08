import re
from userAdmin import *
from commandExecutors import *

class CommandKernel:
    def __init__(self, userList: list) -> None:
        self.commandPatterns = {
            "argumentPattern": re.compile(r'[A-Za-z0-9_\-\.]+|\$[A-Za-z][A-Za-z0-9_]*|".*"'),
            "complexArgumentPattern": re.compile(r'".*"'),
            "variableArgumentPattern": re.compile(r'\$[A-Za-z][A-Za-z0-9_]*'),
            "modifiersPattern": re.compile(r'-[A-Za-z]+')
        }
        self.users = userList

    def getCommand(self, user = "defaltUser", userVariables = {}, tempVariables = {}) -> bool:
        userInput = input(f"{user} >> ")

        arguments = self.commandPatterns["argumentPattern"].findall(userInput)

        complexArguments = self.commandPatterns["complexArgumentPattern"].findall(userInput)
        variableArguments = self.commandPatterns["variableArgumentPattern"].findall(userInput)

        modifiers = self.commandPatterns["modifiersPattern"].findall(userInput)

        for index, item in enumerate(arguments):
            if item in complexArguments:
                arguments[index] = item[1:-1]

            elif item in variableArguments:
                arguments[index] = tempVariables.get(item[1::]) if tempVariables.get(item[1::]) else userVariables.get(item[1::])

        return {"user": user, "arguments": arguments, "modifiers": modifiers}

    def runCommand(self, command: dict):
        match command["arguments"][0]:
            case "encrypt":
                result = encrypt(command["arguments"][1],
                                getKey(command["arguments"][2]))
                print(result)

            case "decrypt":
                result = decrypt(command["arguments"][1],
                                getKey(command["arguments"][2]))
                print(result)

            case "setVariable":
                if command.get("modifiers"):
                    match command["modifiers"][0]:
                        case "-store":
                            userAdmin.storeVariable(
                                command["arguments"][1], command["arguments"][2])
                        case _:
                            pass
                else:
                    command["tempVariables"].update(
                        {command["arguments"][1]: command["arguments"][2]})

            case "switchUser":
                userAdmin.switchUser()

            case _:
                pass
        