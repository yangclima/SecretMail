from encrypt import *
from interface import *
from inputProcess import *
from database import UserVariables

variables = UserVariables().variables

menuGeral = createMenu(
    [
        "Criptografar  mensagem", 
        "Descriptografar mensagem"
    ],

    [
        encrypt, 
        decrypt
    ],

    [
        ["input('Insira a mensagem: ')", "getKey()"], 
        ["input('Insira a mensagem: ')", "getKey()"]
    ]
)

while True:
    userInput = commandDetector(input(">> "), variables)
    result = ""

    match userInput[0]:
        case "encrypt":
            result = encrypt(userInput[1], getKey(userInput[2]))
            print(result)
            
        case "decrypt":
            result = decrypt(userInput[1], getKey(userInput[2]))
            print(result)

        case "setVariable":
            variables.update({userInput[1]: userInput[2]})

