import datetime

def check_birthdate(year, month, day):
    if (int(month) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) <= 31):
        given_date = datetime.datetime.strptime('{}/{}/{}'.format(day,month,year), "%d/%m/%Y").date()
        if given_date > datetime.date.today():
            return False
        else:
            return True
    else:
        return False

def calculate_age(year,month,day):
      
     given_date = datetime.datetime.strptime('{}/{}/{}'.format(day,month,year), "%d/%m/%Y").date()
     difference = datetime.date.today() - given_date
     difference = difference.days
     print("You are {} years, {} months, and {} days".format(int((difference/365)),int((difference%365)/30),(difference%365)%12))
    


year = input("Enter year of birth: ")
month = input("Enter month of birth: ")
day = input("Enter day of birth: ")

valid = check_birthdate(year,month,day)
if valid:
    calculate_age(year,month,day)
else:
    print("You've entered an invalid date")
        
         
