import pandas as pd
data=[100,200,300,400]
names=['kousik','rahul','ravi','ramesh']
result=pd.Series(data,index=names)
new_index=['krish','karthik','kings','american']
final_result=result.reindex(new_index)
print(final_result)