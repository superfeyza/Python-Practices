# Python-Practices
I'm adding some basic "python practices", questions and solution codes.  Practicing while having fun is the best part of learning.


**First Practice:**
1. Let's calculate in which year you will be 100 years old:
2. First of all, to take the instant date, I'll import a libarary which is 
3. >> from datetime import date
4. When we run this code, we see the instant date:
5.  >> today = date.today() 
6.  >> print("date:", today)
7. You will see the date as year-month-day. If you want to write as Day-Month-Year:
8.  >> day_month_year = today.strftime("%d/%m/%Y") 
9. Since our goal is to find out which year we will be 100 years old, let's take the year from the date (day_month_year):
10. >> year = int(day_month_year[6:10]) #We made the year which is the string an integer
11. >> print(f"We are now in {year}")  # Output will be "We are in the year <year> now."
12. Let's edit the code we write for the user, get some information from the user to reach the result:
13. >> name = input("What is your name: ")
14. >> age = int(input("How old are you: ")) 
15. Now that we know the age and date of the user, let's write the final code using a little bit mathematical equation:
16. >> a = str((year-age)+100) 
17. >> print(name + " will be 100 years old in the year " + a)

 
**Second Practice:**
1. In this practice, we will write a code to generate passwords with random letters and numbers.
2. First of all, let's start by importing the "random" and "string" modules.
3. >> import random
4. >> import string
5. Then we use the "ASCII" method so that the algorithm can assign random characters from lowercase, uppercase and numbers to us.
6. >> lower = string.ascii_lowercase #for lowercase
7. >> upper = string.ascii_uppercase #for uppercase
8. >> num = string.digits #for numbers
9. Now we can combine the characters from lowercase, uppercase, and numbers into a password.
10. >> all = lower + upper + num
11. We can also ask the user how many characters the password they want to create should be.
12. >> lenght = int(input("Enter the password lenght you want:"))
13. To complete the process, we generate a random, user-selected template of the length.
14. >> template = random.sample(all,lenght)
15. >> password= "".join(template)
16. With the Join() method we take all the elements in an iterable and concatenate them into a single string.
17. Last step, let's print the password.
18. >> print(password)



**Third Practice:**

  
