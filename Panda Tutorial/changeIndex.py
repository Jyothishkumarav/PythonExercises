# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
df2 = pd.DataFrame({"day":[1,2,3,4],"visitors":[100,200,300,400],"bounce":[10,20,40,60]})
#df1 = pd.DataFrame({"HPI":[8,9,7,6],"int_rate":[200,100,200,400],"IND_GDP":[50,45,45,67]})
print(df2)
#set the index
df2.set_index("day", inplace = True)
#df2.plot();
#plt.show()
#print(df2)
#change the column headers
df2.rename(columns={"visitors":"users"})
print(df2)