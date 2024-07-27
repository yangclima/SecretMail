UNICODE_LEN = 1114111
VALID_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ÁÀÂÃÉÊÍÓÔÕÚÇáàâãéêíóôõúç.,;:!?()[]{}/-_+=*&%$#@^~`<>| "

NUMBER_OF_VALID_CHARACTERS = len(VALID_CHARACTERS)

def getKey(str: str) -> list:
    key = str.split(".")
    for index, item in enumerate(key):
        if item.isdigit():
            key[index] = int(item)
        else:
            print("Invalid key!")
            return getKey()
    return key

def encrypt(msg: str, key: list):
    msg = [VALID_CHARACTERS.index(i) for i in msg]
    a = 0
    for index, item in enumerate(msg):
        msg[index] = item + key[a]

        if msg[index] >= NUMBER_OF_VALID_CHARACTERS:
            msg[index] -= NUMBER_OF_VALID_CHARACTERS

        a += 1
        if a >= len(key):
            a = 0
        
    msg = [VALID_CHARACTERS[i] for i in msg]

    result = ""
    for item in msg:
        result += item

    return result


def decrypt(msg: str, key: list):
    msg = [VALID_CHARACTERS.index(i) for i in msg]
    a = 0
    for index, item in enumerate(msg):
        msg[index] = item - key[a]

        a += 1
        if a >= len(key):
            a = 0

    msg = [VALID_CHARACTERS[i] for i in msg]

    result = ""
    for item in msg:
        result += item

    return result
