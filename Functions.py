def eMobilis():
    print("eMobilis is a tech institute.")


eMobilis()


def addtwonum():
    num = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum of {num} and {num2} is: {num + num2} ")


addtwonum()


def combined():
    num1 = int(input("Enter first number: "))
    num3 = int(input("Enter second number"))
    print(f"The difference of {num1} and {num3} is: {num1 - num3} ")
    print(f"The product of {num1} and {num3} is: {num1 * num3} ")
    print(f"The quotient of {num1} and {num3} is: {num1 / num3} ")


combined()


# function_parameters
def safarimidclass(name, gender, age):
    print(f"Your name is {name} and your age is {age} years old and I am a {gender} person.")


safarimidclass('Emmanuel', 'Male', 25)
safarimidclass('Samuel', 'male', 34)
safarimidclass('Denis', 'male', 26)
safarimidclass('Sydney', 'female', 16)
safarimidclass('Rose', 'female', 30)
