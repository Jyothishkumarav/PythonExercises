# -*- coding: utf-8 -*-
import pandas as pd
xyz_web = {'day':[1,2,3,4,5,6],'visitors':[2000,3000,5000,8000,9000,2000],'bounce_visitor':[350,400,250,200,190,200]}
datframe = pd.DataFrame(xyz_web)
print(datframe)
# slicing starting 2 rows
print(datframe.head(2))
#slicing last 2 rows
print(datframe.tail(2))


