marks = int(input("Enter marks: "))
if marks >=80 and marks <=100:
    print("You have an A")
elif marks >=60 and marks <=79:
    print("You have a B")
elif marks >=40 and marks <=59:
    print("You have a C")
elif marks >=0 and marks <=39:
    print("You have terribly fail")
else:
    print("Wrong Input")

Height = float(input("Enter your height:"))
Weight = float(input("Enter your Weight[Kgs]:"))
bmi = Weight / (Height**2)
if bmi < 13.8:
    print("Underweight")
elif bmi > 25.6 and bmi < 60.8:
    Category = "Overweight"
else:
    category = "Obese"
    print(f"Your BMI is {bmi:.2f} and your classification is {category}")