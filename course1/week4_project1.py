"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    print("this month:", datetime.date(year,(month),1))
    if month==12:
        days = (datetime.date(year, month, 1) - datetime.date(year+1, 1, 1)) * -1
        # print("next month:", datetime.date(year+1, 1, 1))
    else:
        days = (datetime.date(year,month,1) - datetime.date(year,(month+1),1))*-1
        # print("next month:", datetime.date(year,(month+1),1))
    return days.days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year>=datetime.MINYEAR and year<=datetime.MAXYEAR and month>0 and month<13:
        valid_days = days_in_month(year, month)
        return day>0 and day<=valid_days
    return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if not is_valid_date(year1,month1,day1) or (not is_valid_date(year2,month2,day2)):
        return 0
    date1 = datetime.date(year1,month1,day1)
    date2 = datetime.date(year2,month2,day2)
    if date1 > date2:
        return 0
    return (date2 - date1).days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if not is_valid_date(year,month,day):
        return 0
    date = datetime.date(year,month,day)
    today = datetime.date.today()
    if date > datetime.date.today():
        return 0
    return days_between(year,month,day, today.year, today.month, today.day)




def main():
    """
    main program to keep test and functions clean
    :return:
    """
    print("Days in 2018, 2: ",days_in_month(2018,2))
    print("Days in 2018, 1: ",days_in_month(2018,1))
    print("Days in 2017, 12: ",days_in_month(2017,12))
    print("2017,12,33 is valid? ",is_valid_date(2017,12,33))
    print("2017,12,31 is valid? ",is_valid_date(2017,12,31))
    print("1,1,1 is valid? ",is_valid_date(1,1,1))
    print("Days between 2017,12,1, 2017,12,2: ", days_between(2017,12,1, 2017,12,2))
    print("Days between 2017,12,1, 2018,12,1: ", days_between(2017,12,1, 2018,12,1))
    print("Days between 2017,12,2, 2017,12,2: ", days_between(2017,12,2, 2017,12,2))
    print("Days between 2017,12,2, 2017,12,1: ", days_between(2017,12,2, 2017,12,1))
    print("Age for BDay 1970,9,11", age_in_days(1970,9,11))
    print("Age for BDay 2018,3,1", age_in_days(2018,3,1))
    print("Age for BDay 2018,4,1", age_in_days(2018,4,1))


if __name__ == "__main__":
    main()


