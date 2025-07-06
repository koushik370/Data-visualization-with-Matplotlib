from abc import ABC, abstractmethod
class Vechile(ABC):
     def __init__(self,n):
          self.no_of_types=n
     @abstractmethod
     def start(self):
           pass
     def display(self):
           print("HI iam calling from vechile class")