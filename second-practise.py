""" Password Generator """
import random 
import string

print("Hello, Welcome to Password generator")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits

all = lower + upper + num 
lenght = int(input("Enter the password lenght you want:"))

temp = random.sample(all,lenght)
password= "".join(temp)
print(password)
