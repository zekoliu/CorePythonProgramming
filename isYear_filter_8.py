
def isYear(year):
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

all_year = [2001, 2002, 2003, 2004, 2010, 2016]
print filter(isYear, all_year)