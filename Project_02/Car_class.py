class Car:
    def __init__(self,vehicle_type,brand,price):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.price = price
        
    def __str__(self):
        return f"Car details: Vehicle type-{self.vehicle_type},Brand name-{self.brand},Price-Rs.{self.price}"
    
    @classmethod
    def get(cls):
        vehicle_type = input("enter vehicle type: ")
        brand = input("Enter brand name: ")
        price = int(input("Enter car price: "))
        return cls(vehicle_type,brand,price)
    
def main():
    car_1 = Car.get()
    car_2 = Car.get()
    car_3 = Car.get()
    car_4 = Car.get()
    print(f"{car_1}\n{car_2}\n{car_3}\n{car_4}")
    
if __name__ == "__main__":
    main()