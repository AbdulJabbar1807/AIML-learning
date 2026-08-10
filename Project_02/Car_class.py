class Car:
    def __init__(self,vehicle_type,brand,price):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.price = price
        
    def __str__(self):
        return f"Car details: Vehicle type-{self.vehicle_type},Brand name-{self.brand},Price-Rs.{self.price}"
    
def main():
    car_1 = Car("SUV","BMW",8000000)
    print(car_1)
    
if __name__ == "__main__":
    main()