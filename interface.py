from encrypt import *

def createMenu(labels: list, functions: list, arguments: list, menuTitle="Select an option: "):
    def menu():
        if len(labels) != len(functions) or len(labels) != len(arguments):
            raise OSError('operation failed')

        print(menuTitle)
        for index, label in enumerate(labels):
            print(f"[{index + 1}] - {label}")

        selection = int(input(">> "))
        while (selection > len(labels)) or (selection < 1):
            print("Invalid!")
            selection = int(input(">> "))

        return functions[selection - 1](*[eval(i) for i in arguments[selection - 1]])
    
    return menu
