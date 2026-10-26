
def isLeapYear(year):
    # Check leap year conditions
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not a Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"


# Get input and display result
year = int(input()) if False else 2000
print(year, isLeapYear(year))
