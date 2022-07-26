name = input('Enter txt name: ')
text = input('Enter text: ')


import codecs


with codecs.open(f'{name}.txt','w','utf-8') as f:
    f.write(text)
    f.close()