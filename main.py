import os
import codecs
from createCode import createCode

global length

encoding = {}
while True:
    try:
        if os.path.exists(os.path.dirname(os.path.realpath(__file__))+'\coding.txt'):
            print('Successfully found coding.txt. Reading cypher')
            with codecs.open('coding.txt', 'r', 'utf-8') as f:
                # f.read('coding.txt')
                lines = f.readlines()
                # print(lines)
                length = lines[1].index('\n') - 2
                for i in range(1, len(lines)):
                    encoding[lines[i][0]] = lines[i][2:length+2].strip('\n')
                f.close()
                break
        elif not os.path.exists(os.path.dirname(os.path.realpath(__file__))+'\coding.txt'):
            print('Couldn`t find coding.txt, creating it...')
            while True:
                length = input('Input the length of replacable symbol: ')
                try:
                    if int(length) > 1:
                        createCode(int(length))
                        break
                    elif int(length) <= 1:
                        print("Input number which is greater than 1")
                except Exception() as e:
                    pass
    except Exception as e:
        print(e)


testString = input('Input string to cypher: ')


def cypher(string):
    workArray = list(string)
    # print(workArray)
    res = []
    resString = ''
    for i in range(0, len(workArray)):
        # print(encoding[workArray[i]])
        res.append(encoding[workArray[i]])
    for i in range(0, len(res)):
        resString += res[i]
    return resString


def decypher(cypher):
    keyList = list(encoding.keys())
    #print(f'keylist : {keyList}')
    valueList = list(encoding.values())
    #print(f'valuelist : {valueList}')
    resString = ''
    for i in range(length, len(cypher)+length, length):

        if cypher[i-length:i] in encoding.values():
            resString += keyList[valueList.index(cypher[i-length:i])]

    return resString


cypherString = cypher(testString)
decypherString = decypher(cypherString)
print(
    f'CypherString is:\n{cypherString}\nDecypherString is:\n{decypherString}')
