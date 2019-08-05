from datetime import date
from datetime import datetime

def check_birthdate(Year, Month, Day):
	

	users_date= date(Year, Month, Day)
	todays_date=date.today()
	if (users_date< todays_date):
		calculate_age(Year, Month, Day)
		return True

	else:
		print("The birthdate is invalid")
		return False


def calculate_age(Year, Month, Day):
	
	today= date.today()
	user_age_year= today.year - Year
	user_age_month= today.month - Month
	user_age_day= abs(today.day - Day)

	print("you are {} years, {} months, and {} days old".format(user_age_year,user_age_month,user_age_day))


year=int(input("Year of birth? "))
month=int(input("Month of birth? "))
day=int(input("Day of birth? "))
check_birthdate(year, month, day)