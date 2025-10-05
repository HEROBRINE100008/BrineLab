def is_year_leap(year):
    if year < 1582:
        print("No esta dentro del período del calendario Gregoriano")
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False

def days_in_month(year, month):
    if not (1 <= month <= 12) or year < 1:
        return None 
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    

print(day_of_year(2000, 12, 31))