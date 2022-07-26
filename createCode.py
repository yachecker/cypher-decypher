import random
global chars
chars = ',`qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM;\'1234567890@#$%^&*()!йцукенгшщзфывапролдяячсмитьбюЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬБЮ'
global whitespace
whitespace = ''

def randomChars(stringLength):
    global chars
    string = ''
    global whitespace
    for i in range(0,stringLength):
        whitespace += chars[random.randint(0,len(chars)-1)] 
    for i in range(0, stringLength):
        string += chars[random.randint(0, len(chars)-1)]
    return string


symbols = {}
import codecs

def createCode(stringLength):
    global whitespace
    for i in range(0, len(chars)):
        symbols[chars[i]] = randomChars(stringLength)
    with codecs.open(f'coding.txt', 'w','utf-8') as f:
        f.write(f'coding code:\n')
        for key in symbols:
            f.write(f'{key}={symbols[key]}\n')
        f.write(f' ={whitespace}')


if __name__ == '__main__':
    while True:
        length = input('Input the length of replacable symbol: ')
        try:
            length = int(length)
            break
        except ValueError:
            print("Input int only")
    createCode(int(length))
    print(f'Created code with symbol length: {length}')
