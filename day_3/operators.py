
#               ASSIGNMENT OPERATORS

#   Operators          Examples           Same As
    #   =               x  = 5            x = 5
    #   +=              x += 3            x = x + 3
    #   -=              x -= 3            x = x - 3
    #   *=              x *= 3            x = x * 3
    #   /=              x /= 3            x = x * 3
    #   %=              x %= 3            x = x % 3
    #   //=             x //= 3           x = x // 3
    #   **=             x **= 3           x = x ** 3  
    #   &=              x &= 3            x = x & 3
    #   |=              x |= 3            x = x | 3
    #   ^=              x ^= 3            x = x ^= 3
    #   >>=             x >>= 3           x = x >> 3
    #   <<=             x <<= 3           x = x << 3 



#                   ARITHMETIC OPERATORS

#   Addition        ->      +
#   Subtraction     ->      -
#   Multiplication  ->      *
#   Division        ->      /
#   Modulus         ->      %
#   Floor Division  ->      //
#   Exponentiation  ->      **


#   Operators          Name           Example
    #   +             Addition            x + y
    #   -             Subtraction         x - y
    #   *             Multiplication      x * y
    #   /             Division            x / y
    #   %             Modulus             x % y
    #   **            Exponentiation      x ** y
    #   //            Floor division      x // y


#   Arithmetic Operators in Python
#   Integers

print('Addition: ', 1 + 2)          # 3
print('Subtraction: ', 2 - 1)       # 1
print('Multiplication: ', 2 * 3)    # 6  
print('Division: ', 4 / 2)          # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)          # 3.0  Division in Python gives floating number
print('Division: ', 7 / 2)          # 3.5  Division in Python gives floating number
print('Division without the remainder: ', 7 // 2)   # 3, gives without the floating number without the remainder
print('Division without the remainder: ', 7 // 3)   # 2 
print('Modulus: ', 3 % 2)           # 1, Gives the remainder
print('Exponentiation: ', 2**3)     # 8 it means 2 * 2 * 2



#       Floating numbers
print('Floating point number, PI', 3.14)
print('Floating point number, gravity', 9.81)   #   9.81 meters per second squared


#       Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 +1j) * (1 -1j))
    

#       Calculating area of circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print( 'Area of a circle: ', area_of_circle)


#       Calculating area of rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)

#       Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity         # Adding unit to the weight
print (weight, 'N')


#       Calculate the density of s liquid
mass = 75   # in Kg
volume = 0.075              # in cubic meter
density = mass / volume     # 1000 Kg/m^3
print(density)



#       COMPARASION OPERATOR


#   Operators               Name                    Example

#       ==          Equal                           x == y
#       |=          Not equal                       x != y
#       >           Greater than                    x > y
#       <           Less than                       x < y
#       >=          Greater than or equal to        x >= y
#       <=          Less than or equal to           x <= y


print(3 > 2)    # True
print(3 >= 2)   # True
print(3 < 2)    # False
print(2 < 3)    # True
print(2 <= 3)   # True
print(3 == 2)   # False
print(3 != 2)   # True
print(len('mango') == len('avocado'))   # False
print(len('mango') != len('avocado'))   # True
print(len('mango') < len('avocado'))    # True
print(len('milk') != len ('meat'))      # False
print(len('milk') == len('meat'))       # True
print(len('tomate') == len('potato'))   # True
print(len('python') > len('dragon'))    # True


#       Comparing something gives either a True o False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False: ', False == False)



# Además del operador de comparación anterior, Python usa:

#       is : Devuelve "True" si ambas variables son el mismo objecto (x is y)
#       is not : Devuelve "True" si ambas variables no son el mismo objeto (x is not y)
#       in : Devuelve "True" si la lista consultada contiene un determinado elemento
#       not in : Devuelve "True" si la lista consulata no tiene un determinado elemento

print ('1 is 1', '1 is 1')                  # True - because de data values are the same
print ('1 is not 2', '1 is not 2')          # True - because 1 is not 2
print ('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
print ('B in Asanemeh', 'B' in 'Asabeneh')  # False - there is no uppercase B
print ('coding' in 'coding for all')        # True - because coding for all has the word coding
print ('a in an:', 'a' in 'an')             # True
print ('4 is 2 ** 2:', 4 is 2 ** 2)         # True




#           LOGICAL OPERATOR

 #  OPERATOR        DESCRIPTION                                                 EXAMPLE
 #  and             Returns True if both statements are tre                     x > 5 and x < 10
 #  or              Returns True if one of the statements is true               x < 5 or x < 4
 #  not             Reverse the result, return False if the result is true      not (x < 5 and x < 10) the result is true


print(3 > 2 and 4 > 3)  # True
print(3 > 2 and 4 < 3)  # False
print(3 < 2 and 4 < 3)  # False
print('True and True: ', 'True and True')
print(3 > 2 or 4 > 3)   # True
print(3 > 2 or 4 < 3)   # True
print(3 < 2 or 4 < 3)   # False
print('True or False: ', 'True or False')
print(not 3 > 2)        # False
print(not True)         # False
print(not False)        # True
print(not not True)     # True
print(not not False)    # False

