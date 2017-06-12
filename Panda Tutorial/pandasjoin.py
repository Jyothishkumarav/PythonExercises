# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd
df1=pd.DataFrame({"int_rate":[2,1,2,4],"IND_GDP":[50,45,45,67]},index =[2001,2002,2003,2005])
df2=pd.DataFrame({"hpi":[2,1,2,4],"un_emo":[250,45,45,67]},index =[2002,2003,2004,2005])
print(df1)
print(df2)
joined = df1.join(df2);
print(joined)


