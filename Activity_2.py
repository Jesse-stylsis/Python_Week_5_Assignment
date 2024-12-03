# Base class for Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Car class inheriting from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving ")

# Plane class inheriting from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ")

# Create objects of Car and Plane
car = Car()
plane = Plane()

# Call the move method for each object
car.move()  # Outputs: Driving 
plane.move()  # Outputs: Flying 
