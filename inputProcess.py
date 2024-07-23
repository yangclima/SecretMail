def commandDetector(userInput: str) -> list:
    userInput = list(userInput)

    argumentList = []
    argument = ""

    oppenedArgument = False
    scapeChracter = False

    for index, item in enumerate(userInput):

        if item == "\\":
            scapeChracter = True
            continue

        if scapeChracter:
            argument = argument + userInput[index]

        # Detecta o fechamento do argumento
        if oppenedArgument and item == '"':
            oppenedArgument = False
            continue
        
        # Adiciona qualquer caractere indiscriminadamente enquanto houver um argumento aberto
        if oppenedArgument:
            argument = argument + userInput[index]
            continue

        # Detectada que o argumento está finalizado por um espaço
        if item == " ":
            argumentList.append(argument)
            argument = ""

        elif index == len(userInput) - 1:
            argument = argument + userInput[index]
            argumentList.append(argument)

        # Detecta a abertura de um argumento
        elif item == '"':
            oppenedArgument = True
        # Adiciona os caracteres 
        else:
            argument = argument + userInput[index]

    return argumentList