# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:33:18 2023

@author: mhouts
"""

#------------------------------------------------------------------------------
# Exercise 1 Create a Class with instance attributes
#------------------------------------------------------------------------------
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
car1 = Vehicle(200, 100000)

print(car1.mileage)

#------------------------------------------------------------------------------
# Exercise 2 Create a Vehicle class without any variables and methods
#------------------------------------------------------------------------------
class Vehicle:
    pass

#------------------------------------------------------------------------------
# Exercise 3 Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
#------------------------------------------------------------------------------
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
bus = Vehicle('Line 66', 130, 30000)
print(bus.name, bus.max_speed, bus.mileage)

#------------------------------------------------------------------------------
# Exercise 4 Class Inheritance
#------------------------------------------------------------------------------
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

bus = Bus('Line 66', 130, 30000)
print(bus.seating_capacity())

#------------------------------------------------------------------------------
# Exercise 5 Define a property that must have the same value for every class instance (object)
#------------------------------------------------------------------------------
class Vehicle:
    color = 'White'
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus('School Volvo', 180, 12)
car = Car('Audi Q5', 240, 18)

print(bus.color,bus.name,bus.max_speed,bus.mileage)
print(car.color,car.name,car.max_speed,car.mileage)

#------------------------------------------------------------------------------
# Exercise 6 Class Inheritance
#------------------------------------------------------------------------------
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 0.1
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

#------------------------------------------------------------------------------
# Exercise 7 Check type of an object
#------------------------------------------------------------------------------
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))

#------------------------------------------------------------------------------
# Exercise 8 Determine if School_bus is also an instance of the Vehicle class
#------------------------------------------------------------------------------
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus, Vehicle))
