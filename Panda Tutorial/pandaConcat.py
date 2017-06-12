# -*- coding: utf-8 -*-
import pandas as pd
df1=pd.DataFrame({"HPI":[80,90,70,60],"int_rate":[2,1,2,4],"IND_GDP":[50,45,45,67]},index =[2001,2002,2003,2004])
df2=pd.DataFrame({"HPI":[80,90,70,50],"int_rate":[2,1,2,4],"IND_GDP":[50,45,45,67]},index =[2005,2006,2007,2004])
print(df1)
print(df2)
merge = pd.concat([df1,df2])
print(merge)

