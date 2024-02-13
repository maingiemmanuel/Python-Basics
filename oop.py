class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def describe_car(self):
        print(f"My dream car is a {self.color} {self.make} and my model is {self.model} manufactured in {self.year}")


my_obj = Car("Volkswagen", "MK8.5", "2024", "red")
my_obj2 = Car("Audi", "Q5", 2023, "white")
my_obj.describe_car()
my_obj2.describe_car()