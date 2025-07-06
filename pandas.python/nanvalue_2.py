import pandas as pd
data=[10,20,30,40,50]
lables=['koushik','ramesh','rahul','ravi','ramakrishna']
result=pd.Series(data,index=lables)
print(result)
final=result[2]
print(final)