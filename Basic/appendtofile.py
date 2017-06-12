# -*- coding: utf-8 -*-
appendMe = '\nNew bit of information'

appendFile = open('C:\\test.txt','a')
appendFile.write(appendMe)
appendFile.close()
