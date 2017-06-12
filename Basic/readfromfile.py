# -*- coding: utf-8 -*-

textfile = open('C:\\test.txt','r').readlines()

for text in textfile:
    print(text)
textfileread = open('C:\\test.txt','r').read()
print(textfileread)

