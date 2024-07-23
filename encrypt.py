UNICODE_LEN = 1114111

def getKey() -> list:
    key = input("Insira a Chave: ").split(".")
    for index, item in enumerate(key):
        if item.isdigit():
            key[index] = int(item)
        else:
            print("Chave Inválida!")
            return getKey()
    return key

def encrypt(msg: str, key: list):
    msg = [ord(i) for i in msg]
    a = 0
    for index, item in enumerate(msg):
        msg[index] = item + key[a]

        if msg[index] >= UNICODE_LEN:
            msg[index] -= UNICODE_LEN

        a += 1
        if a >= len(key):
            a = 0
        
    msg = [chr(i) for i in msg]

    result = ""
    for item in msg:
        result += item

    return result


def decrypt(msg: str, key: list):
    msg = [ord(i) for i in msg]
    a = 0
    for index, item in enumerate(msg):
        msg[index] = item - key[a]

        a += 1
        if a >= len(key):
            a = 0

    msg = [chr(i) for i in msg]

    result = ""
    for item in msg:
        result += item

    return result
