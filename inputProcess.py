import re

argsPattern = re.compile(r'".+"|[a-zA-Z0-9\.]+|\$[a-zA-Z]+[a-zA-Z0-9_]*')
complexArgsPatern = re.compile(r'".+"')
variableArgsPattern = re.compile(r'\$[a-zA-Z]+[a-zA-Z0-9_]*')

def commandDetector(userInput: str, UserVariables: dict = {}) -> list:
    args = argsPattern.findall(userInput)
    complexArgs = complexArgsPatern.findall(userInput)
    variableArgs = variableArgsPattern.findall(userInput)
    
    for index, item in enumerate(args):
        if item in complexArgs:
            args[index] = item[1:-1]
        if item in variableArgs:
            args[index] = UserVariables.get(item[1::])

    return args