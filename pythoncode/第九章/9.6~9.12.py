#9.6
# class Restaurant():
#     def __init__(self, restaruant_name, cuisine_type):
#         self.name = restaruant_name
#         self.type = cuisine_type
    
#     def describe_restaurant(self):
#         print(f"The restaurant's name is {self.name}")
#         print(f"The {self.name} is {self.type}")
    
#     def open_restaurant(self):
#         print(f"\n{self.name} is opening")
# class IceCreamStand(Restaurant):
#     def __init__(self, restaruant_name, cuisine_type):
#         super().__init__(restaruant_name, cuisine_type)
#         self.flavors = ['香草','巧克力','抹茶']
#     def ice_favors(self):
#         for i in self.flavors:
#             print(i)

# iceCreamStand = IceCreamStand('宜家','冰淇淋店')
# iceCreamStand.ice_favors()


#9.7
# class User:
#     def __init__(self,first_name,last_name,age,work_place):
#         self.firstname = first_name
#         self.lastname = last_name
#         self.age = age
#         self.workplace = work_place

#     def describe_user(self):
#         print(f"\nfirstname: {self.firstname}")
#         print(f"lastname: {self.lastname}")
#         print(f"age: {self.age}")
#         print(f"workplace: {self.workplace}")
    
#     def greet_user(self):
#         print(f"Hello {self.firstname}{self.lastname},welcom.")

# class Admin(User):
#     def __init__(self, first_name, last_name, age, work_place):
#         super().__init__(first_name, last_name, age, work_place)
#         self.privileges = ["can add post", "can delete post", "can ban user"]
    
#     def show_privileges(self):
#         print(f"{self.firstname}{self.lastname} have these privileges: ")
#         for i in self.privileges:
#             print(i)

# # admin = Admin("周","宇鸿",23,"武汉")
# # admin.show_privileges()


#9.8   
# class Privileges:
#     def __init__(self):
#         self.privileges = ["can add post", "can delete post", "can ban user"]
    
#     def show_privileges(self):
#         for i in self.privileges:
#             print(i)

# class Admin(User):
#     def __init__(self, first_name, last_name, age, work_place):
#         super().__init__(first_name, last_name, age, work_place)
#         print(f"{self.firstname}{self.lastname} has these privileges: ")
#         self.privileges = Privileges()

# admin = Admin("周","宇鸿",23,"武汉")
# admin.privileges.show_privileges()

#9.9
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

# class Battery:
#     def __init__(self,batter_size = 40):
#         self.battery_size = batter_size
    
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kwh battery")

#     def get_range(self):
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225
#         print(f"This car can go about {range} miles on a full charge.")
    
#     def upgrade_battery(self):
#         if self.battery_size != 65:
#             self.battery_size = 65


# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()

# car = ElectricCar('byd','秦',2024)
# car.battery.get_range()
# car.battery.upgrade_battery()
# car.battery.get_range()


# from restaurant import Restaurant as RT
# restaurant = RT('肯德基','炸鸡快餐')
# restaurant.describe_restaurant()

# from upa import Admin
# admin = Admin('周','宇鸿',23,'武汉')
# admin.privileges.show_privileges()

# from pa import Admin
# admin = Admin('周','宇鸿',23,'武汉')
# admin.privileges.show_privileges()