import math

#   'Day 2: 30 DAys of python programming'

# Exercises Level 1
from math import pi
from xml.etree.ElementTree import PI


first_name = 'luis'
last_name = 'camacho'
full_name = 'Luis Camacho'
country = 'Spain'
city = 'Madrid'
age = 250
year = 2015
is_married = False
is_true = True
is_light = True
eyes, height, weight = 'green', 80, 169


# Ejercises Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light))
print(eyes, height, weight)

print(len(first_name))
more = print(len(first_name)>(len(last_name)))
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_two-num_one
print(diff)
product = num_one*num_two
print (product)
division = num_one/num_two
print(division)
exp = num_one**2
print(exp)
floor_division = num_one//num_two
print(floor_division)

# 5. The Radius of a circle is a 30 meters
radius = 30

#   I Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = math.pi*radius**2          #   Área = PI * radio^2
print("The área of circle is ",area_of_circle)


#   II Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = math.pi * (radius*2)     #   Circunferencia = PI * diametro
print("The circum of circle is ",circum_of_circle)

# III Take radius as user input and calculate the area.
radius_user = int(input("Enter the radius of circle: "))
area = math.pi*radius_user**2
print(area)

#   6.  Use the built-in input function to get first name, last name, country and age from a user 
#       and store the value to their corresponding variable names

first_name = input("Whats your name?: ")
last_name  = input("Whats your last name? ")
country = input("What is your country? ")
age = input("How old are you?")
print(f"Hi {first_name} {last_name}, you have a {age} years old and you're from {country}")




