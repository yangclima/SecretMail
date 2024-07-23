from encrypt import *
from interface import *
from inputProcess import *

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
    userInput = commandDetector(input(">> "))
    result = ""

    match userInput[0]:
        case "encrypt":
            result = encrypt(userInput[1], [int(i) for i in userInput[2].split(".")])
        case "decrypt":
            result = decrypt(userInput[1], [int(i) for i in userInput[2].split(".")])

    print(result)