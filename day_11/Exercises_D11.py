import math
import re
import sys

# 1 → Declare a function add_two_numbers. 
# It takes two parameters and it returns a sum
def add_two_numbers(num1, num2):
    return num1+num2

print(add_two_numbers(45, 102))


# 2 → Area of a circle is calculated as follows:area = PI *r²
# Write a function tha calculates area_of_circle

def area_of_circle(r):
    PI = 3.14
    area = PI * r**2
    return area

print(area_of_circle(5))


# 3 → Write a function called add_all_nums 
# which takes arbitrary number of arguments and sums all the arguments
# Check if all the list items are numbers types. If not do given a reasonable feedback


def add_all_nums(*args):
    total = 0
    for num in args:
        total +=num
    return(total)

print(add_all_nums(10,23,24,35))


# Temperature in ºC can be converted to ºF using formula : ºF = (ºC x 9/5)+32 .
# Write a function which converts ºC to ºF, « convert_celsius_to-faenheit »

def convert_celsius_to_fahrenheit (grados):
    return grados*9/5+32

print(convert_celsius_to_fahrenheit(50))

# Convert fahrenheit to celsius

def convert_fahrenheit_to_celsius(grados):
    return (grados-32)*5/9

print(convert_fahrenheit_to_celsius(82))


# 5 → Write a function called check-season, it takes a month parameter and returns the season:
# Autumn → September, October, November
# Winter → December, January, February
# Spring → March, April, May
# Summer → June, July, August

def what_season(month):
    if month > 8 and month < 12:
        return("Autum")
    elif month > 2 and month < 6:
        return("Spring")
    elif month > 5 and month < 9:
        return ("Summer")
    else:
        return("Winter")

print(what_season(8))


# 6 → Write the function called calculate_slop which return the slope of a linear equation
# El cambio vertical entre dos puntos se llama elevación
# El cambio horizontal entre dos puntos se llama avance
# La pendiente es igual a la división de la elevación entre el avance:

def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m








