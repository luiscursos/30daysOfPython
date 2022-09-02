from logging import critical
import math 

age = 40
height = 180.0
complex(1j)


#   4.   Calculate the area of a triangle

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
print ("\nThe area of the triangle is: ", base*height/2)

#   5.   Calculate the perimeter of the triangle

a = int(input("Enter the side 'a': "))
b = int(input("Enter the side 'b': "))
c = int(input("Enter the side 'c': "))
print("The perimeter of the triangle is: ", a + b + c)



#   6. Get lenght and width of a rectangle using prompt. 
#    Calculate its area (area = lenght * width) .
#    Calculate its perimeters (perimeters = 2 * (length * width))

length = int(input("Enter the lenght of a rectangle: "))
width = int(input("Enter the width of a rectangle: "))
area_reactangle = length * width
perimeter_rectangle = (length + width)*2
print("The area of the rectangle is" ,area_reactangle)
print("The perimeter of the triangle is ",perimeter_rectangle)

#   7. Get the radius of a circle using prompt. 
#   Calculate the area (area = pi * r²)
#   Calculate the circunference (circunference = 2 * pi * r )

radius = float(input("Enter a radius of a circle: "))
area_circle = math.pi * radius**2
circunference = 2 * math.pi * radius
print("The area of a circle is ",area_circle)
print("The circunference of a circle is ",circunference)


#   8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
#   9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
#   10. Compare the slopes in tasks 8 and 9.
#   11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#   12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print (len("python"))
print (len("dragon"))
print (not (len("dragon")) == (len("python")))
print ((len("dragon")) == (len("python")))

#   13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python') # Encuentra una subcadena dentro de un string
print('on' in 'dragon')

#   14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
#   15. There is no 'on' in both dragon and python
#   16. Find the length of the text python and convert the value to float and convert it to string
print(float(len("python")))
#   17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input("Enter a number for comprobation: "))
print(num % 2 == 0)
    

#   18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
#   19. Check if type of '10' is equal to type of 10
#   20. Check if int('9.8') is equal to 10
#   21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
rate = 28.0
hours = 8
days = float(input("Enter a days of work: "))
print("The pay is ", float(rate*(hours * days)))
print("The weekly earning is ", float(rate*(hours * days)))



#   22. Write a script that prompts the user to enter number 
#   of years. Calculate the number of second a person can live. 
#   Assume a person can live hundred years
live = 100
seconds = 60 * (60 * (24*365))
print("Your live in seconds...", seconds * live) 

#   23. Write a Python script that display the following table
    # 1 1 1 1 1
    # 2 1 2 4 8
    # 3 1 3 9 27
    # 4 1 4 16 64
    # 5 1 5 25 125 

print(1, 1, 1, 1, 1)
print(2, 1, 2**1, 2**2, 2**3)
print(3, 1, 3**1, 3**2, 3**3)
print(4, 1, 4**1, 4**2, 4**3)
print(5, 1, 5**1, 5**2, 5**3)
