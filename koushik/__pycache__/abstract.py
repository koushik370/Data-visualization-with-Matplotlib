from  module_2 import*
class Bike(Vechile):
      def __init__(self,n,color):
            super().__init__(n)
      def start(self):
             print("start with kick")
class Scooty(Vechile):
      def __init__(self,n):
            super().__init__(n)
      def start(self):
             print("self start")
class Car(Vechile):
       def __init__(self,n,x):
             super().__init__(n)
             self.no_of_gears=6
       def start(self):
             print("start with key")

            