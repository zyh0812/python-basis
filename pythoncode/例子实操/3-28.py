# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         print(f"{self.name} roll over!")

# my_dog = Dog('Whllie', 6)
# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.age} years old")

# my_dog.sit()


# your_dog = Dog('Lucy',3)
# print(f"\nYour dog's name is {your_dog.name}")
# print(f"Your dog is {your_dog.age} years old")
# your_dog.roll_over()

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

# my_new_car = Car('audi','a4',2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.updata_odometer(24)
# my_new_car.read_odomter()
# my_new_car.updata_odometer(13)
# my_used_car = Car('subaru','outback',2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.updata_odometer(23_500)
# my_used_car.read_odomter()

# my_used_car.increment_odometer(100)
# my_used_car.read_odomter()