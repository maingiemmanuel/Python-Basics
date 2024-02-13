class Fruits:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe_fruits(self):
        print(f"I like eating {self.name} which is Kshs. {self.price}.")


my_obj = Fruits("apple", 25)
my_obj2 = Fruits("strawberries", 100)
my_obj3 = Fruits("banana", 5)
my_obj4 = Fruits("pineapple", 50)
my_obj5 = Fruits("mangoes", 20)
my_obj.describe_fruits()
my_obj2.describe_fruits()
my_obj3.describe_fruits()
my_obj4.describe_fruits()
my_obj5.describe_fruits()
