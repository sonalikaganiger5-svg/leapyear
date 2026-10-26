
from leap import isLeapYear

def test_leap_year():
    assert isLeapYear(2024) == "Leap Year"

def test_not_leap_year():
    assert isLeapYear(2025) == "Not a Leap Year"
