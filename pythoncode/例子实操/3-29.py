# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#     def read_odomter(self):
#         print(f"This car has {self.odometer_reading} mils on it.")
    
#     def updata_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 40
    
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kwh battery")

# my_leaf = ElectricCar('nissan','leaf',2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()

# class Battery:
#     def __init__(self,batter_size = 65):
#         self.battery_size = batter_size
    
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kwh battery")

#     def get_range(self):
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225
#         print(f"This car can go about {range} miles on a full charge.")

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()

# my_leaf = ElectricCar('nissan','leaf',2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

# from random import randint
# print(randint(1,6))

# from random import choice
# players = ['charles','martina','michael','florence','eli']
# first_up = choice(players)

# print(first_up)