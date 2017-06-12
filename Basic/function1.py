# -*- coding: utf-8 -*-
def function_sample():
    print('inside the function')
    z = 10 + 10
    print("Result is : " , z)

def sample(num1,num2=5):
    result = num1 + num2
    print(num1,num2,result)

sample(4)
sample(4,50)