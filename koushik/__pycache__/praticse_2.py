#example of operator  overloading 
class Bill:
     def __init__(self,name,age):
           self.name=name
           self.age=age
     def __gt__(self,other):
            if self.age>other.age:
                   return True
            else:
                   return False
info_1=Bill('koushik',19)
info_2=Bill('rithvik',17)
if info_1>info_2:
       print(f"{info_1.name} will pay the bill")
else:
        print(f"{info_2.name} will pay the bill")
