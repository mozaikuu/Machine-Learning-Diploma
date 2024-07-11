class Car:
    def __init__(self, MaxSpeed, SpeedUnit):
        self.MaxSpeed = MaxSpeed
        self.SpeedUnit = SpeedUnit
        
    def CarSpeed():
        return f"Car with the maximum speed of {Car.MaxSpeed} {Car.SpeedUnit}"
        

class Boat:
    def __init__(self, MaxSpeed):
        self.MaxSpeed = MaxSpeed
        
    def BoatSpeed():
        return f"Car with the maximum speed of {Boat.MaxSpeed} {Boat.SpeedUnit}"
      
car = Car(100, "km/h")

    
    def __str__(self):
        return f"Car with the maximum speed of {self.MaxSpeed} {self.SpeedUnit}"
    
car_str = str(car)
