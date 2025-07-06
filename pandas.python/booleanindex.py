import pandas as pd
data=[1,2,3,4]
result=['a','v','c','d']
a=pd.Series(data,index=result)
marks=a>1
final=a[marks]
print(final)