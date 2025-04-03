class Employee:
    def __init__(self,first_name, last_name, salary):
        self.firstname = first_name
        self.lastname = last_name
        self.salary = salary

    def give_raise(self, salary,a = ''):
        salary += 5000
        if a:
            salary = 5000
            salary += a
            return salary



