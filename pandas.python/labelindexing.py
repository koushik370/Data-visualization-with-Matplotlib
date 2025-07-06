import pandas as pd
a=[10,20,30,40]
data=['a','b','c','d']
result=pd.Series(a,index=data)
print(result)