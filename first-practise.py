""" What year will you be 100 years old? """

from datetime import date

today = date.today()

# dd/mm/YY
day = today.strftime("%d/%m/%Y")

year = int(day[6:10])
print(f"We are now in {year}")

name = input("What is your name: ")
age = int(input("How old are you: "))

a = str((year-age)+100)
print(name + " will be 100 years old in the year " + a)
