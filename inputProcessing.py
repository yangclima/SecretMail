import re

argsPattern = re.compile(r'".+"|[a-zA-Z0-9\.]+|\$[a-zA-Z]+[a-zA-Z0-9_]*')
complexArgsPatern = re.compile(r'".+"')
variableArgsPattern = re.compile(r'\$[a-zA-Z]+[a-zA-Z0-9_]*')
modifiersPattern = re.compile(r'-[A-Za-z]+')

def commandDetector(userInput: str, userVariables: dict = {}, tempVariables: dict = {}) -> dict:
    args = argsPattern.findall(userInput)

    complexArgs = complexArgsPatern.findall(userInput)
    variableArgs = variableArgsPattern.findall(userInput)

    modifiers = modifiersPattern.findall(userInput)
    
    for index, item in enumerate(args):
        if item in complexArgs:
            args[index] = item[1:-1]

        elif item in variableArgs:
            args[index] = tempVariables.get(item[1::]) if tempVariables.get(item[1::]) else userVariables.get(item[1::])

    return {"args": args, "modifiers": modifiers}