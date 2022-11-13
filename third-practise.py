""" Calculating Body Mass Index """

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

MBI = weight/(height**2)
print("Your Body Mass Index is: {0:.2f}\n".format(MBI), end='')

if MBI <= 18.4:
    print("You are leaner than the healthy range. For your health, it is recommended to consult a doctor.")
elif MBI <= 24.9:
    print("You are in the healthy BMI range.")
elif MBI <= 29.9:
    print("You are above the healthy range. ")
elif MBI <= 34.9:
    print("You are not in the healthy range. It is recommended to consult a doctor for your health.")
else:
    print("You are outside of the healthy range.! For your health, it is recommended to go to a doctor's control immediately.")
