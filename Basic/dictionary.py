# -*- coding: utf-8 -*-
studentmark = {'jack':[25,580],'jim':[24,400],'ramu':[24,590]}
print(studentmark)
# add
print('Add raju')
studentmark['raju'] = [24,599]
print(studentmark)
print('update raju')
studentmark['raju'] = [24,600]
print(studentmark)    
print("Raju's age is",studentmark['raju'][0])   
print("Raju's Mark is",studentmark['raju'][1])   
print("Deleting Raju")
del studentmark['raju']
print(studentmark)
