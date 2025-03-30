# class Car:
#     def __init__(self,make,model,year):
#         self.make =make
#         self.model = model
#         self.year = year
#         self.odometer_reding = 0
    
#     def get_describe_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reding} miles on it.")
    
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reding:
#             self.odometer_reding = mileage
#         else:
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self,miles):
#         self.odometer_reding += miles

