from datetime import date

def check_birthdate(year, month, day):
    if (int(month) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) <= 31):
        given_date = date(year = int(year), month = int(month), day = int(day))
        if given_date > date.today():
            return False
        else:
            return True
    else:
        return False

def calculate_age(year,month,day):
      
     given_date = date(year = int(year), month = int(month), day = int(day))
     difference = date.today() - given_date
     difference = difference.days
     years = int((difference/365))
     year_int = int(year)
     days_in_each_month = []
     
     while year_int <= 2019:
         if (year_int%4 == 0) and ((not year_int%100) == 0 or (year_int%400 == 0)):
             days_in_each_month.extend((31,29,31,30,31,30,31,31,30,31,30,31))
         else:
             days_in_each_month.extend((31,28,31,30,31,30,31,31,30,31,30,31))
         year_int += 1
             
     months = 0
     for day in days_in_each_month:

         if difference >= day:
             months += 1
             difference -= day
     print("You are {} years, {} months, and {} days".format(years,months%12,difference))

 
year = input("Enter year of birth: ")
month = input("Enter month of birth: ")
day = input("Enter day of birth: ")

valid = check_birthdate(year,month,day)
if valid:
    calculate_age(year,month,day)
else:
    print("You've entered an invalid date")
        
         
