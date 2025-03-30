class Restaurant():
    def __init__(self, restaruant_name, cuisine_type):
        self.name = restaruant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"The {self.name} is {self.type}")
    
    def open_restaurant(self):
        print(f"\n{self.name} is opening")