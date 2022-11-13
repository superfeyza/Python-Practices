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
1. aa
2. bb
3. cc
4.
5.
  
