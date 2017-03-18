# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:23:38 2017

@author: 310251316
"""
def sorting_example(sample_str):
    return len(sample_str),sample_str[0]
    
def sorting_example1(sample_str):
    return sample_str.lo
    
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list(set(a)-set(b))
d = list(set(a) & set(b))
c.sort()
print(c)
print(d)
te = [5, 10, 15, 20, 25, 30, 35, 40]
ce = te[3:0:-1]
print(ce)
print(te[::2])
str="hai helllo how are youuuu hope u are doing great"
print(len(str))
print(str[0:len(str)-8])
list_str=['hai','hello','aaaaaa','how are u','what are u soing','bye','c u']
"""list_str.sort(key=len)"""
#list_str.sort(key= lambda s:len(s))
#list_str.sort(key = sorting_example)
print("before sort\n")
print(list_str)
list_str.sort()
list_str.sort(key = sorting_example)
print("after sort\n")
print(list_str)