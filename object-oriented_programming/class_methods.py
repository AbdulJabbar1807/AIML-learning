import random

class Car:
    brands = ["Tata","BMW","Mahindra","Tesla"]
    
    @classmethod
    def sort(cls,car):
        print(f"{car} brand name is {random.choice(cls.brands)}.")
        
Car.sort("suv")
    

