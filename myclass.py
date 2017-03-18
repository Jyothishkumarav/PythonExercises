# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:34:56 2017

@author: 310251316
"""
class Basecalss:
    def __init__(self,age):
        self.age = age
class Myclass(Basecalss):
    def __init__(self,name,age):
        super().__init__(age)
        self.name = name

myobj=Myclass("jyothish",26)
print(myobj.name)
print(myobj.age)
        