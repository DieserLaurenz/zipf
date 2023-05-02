# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:48:11 2023

@author: laure
"""

if __name__ == "__main__":
    def is_leap_year(year):
        if (year % 4 == 0 and not(year % 100 == 0)) or (year % 100 == 0 and year % 400 == 0):
            return(True)
        else:
            return(False)
        
    tests = [1900, 1984, 1985, 2000, 2018, 2016, 2017, 2020, 2021]
    for test in tests:
        if is_leap_year(test):
            print(f"{test} is a leap year")
        else:
            print(f"{test} is not a leap year")