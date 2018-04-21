
def is_Year(year):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True
    else:
        return False


year = 1900
print is_Year(year)