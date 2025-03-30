# class Restaurant():
#     def __init__(self, restaruant_name, cuisine_type):
#         self.name = restaruant_name
#         self.type = cuisine_type
    
#     def describe_restaurant(self):
#         print(f"The restaurant's name is {self.name}")
#         print(f"The {self.name} is {self.type}")
    
#     def open_restaurant(self):
#         print(f"\n{self.name} is opening")

# the_restaurant = Restaurant('矮子饭馆','赣菜')

# the_restaurant.describe_restaurant()

# the_restaurant1 = Restaurant('王朝饭店','酒席')

# the_restaurant.describe_restaurant()

# the_restaurant2 = RecursionError('江西小炒','赣菜')

# the_restaurant.describe_restaurant()


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

# user1 = User('周','宇鸿',23,'武汉')
# user1.describe_user()
# user1.greet_user()
# user2 = User('刘','嘉文',22,'光谷')
# user2.describe_user()
# user2.greet_user()
# user3 = User('胡','雨蝶',22,'武汉')
# user3.describe_user()
# user3.greet_user()

# class Restaurant():
#     def __init__(self, restaruant_name, cuisine_type):
#         self.name = restaruant_name
#         self.type = cuisine_type
#         self.number_serverd = 0
    
#     def describe_restaurant(self):
#         print(f"The restaurant's name is {self.name}")
#         print(f"The {self.name} is {self.type}")
#         print(f"{self.number_serverd} people had ate.")
    
#     def open_restaurant(self):
#         print(f"\n{self.name} is opening")
    
#     def set_number_serverd(self,pn):
#         self.number_serverd = pn
    
#     def increment_number_served(self,pns):
#         self.number_serverd += pns

# resturant = Restaurant('江西小炒','赣菜')
# resturant.set_number_serverd(2)
# resturant.describe_restaurant()
# resturant.increment_number_served(5)
# resturant.describe_restaurant()


# class User:
#     def __init__(self,first_name,last_name,age,work_place):
#         self.firstname = first_name
#         self.lastname = last_name
#         self.age = age
#         self.workplace = work_place
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"\nfirstname: {self.firstname}")
#         print(f"lastname: {self.lastname}")
#         print(f"age: {self.age}")
#         print(f"workplace: {self.workplace}")
    
#     def greet_user(self):
#         print(f"Hello {self.firstname}{self.lastname},welcom.")
    
#     def increment_login_attmpts(self):
#         self.login_attempts += 1
    
#     def reset_login_attempts(self):
#         self.login_attempts = 0

# user1 =User('周','宇鸿',23,'武汉')
# user1.increment_login_attmpts()
# user1.increment_login_attmpts()
# user1.increment_login_attmpts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)