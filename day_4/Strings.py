#   Creating a String


letter = 'p'
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)


#   Multiline String is created by using triple single (''') or triple double quotes (""").

multiline_string = ''' I am a .....
'''
print(multiline_string)

# Another way of doing the same thing
Other_multiline_string = """ I am a .....
"""
print(Other_multiline_string)


# String concatenation

first_name = 'lucathor'
last_name = 'cathorluca'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))


# Escape Sequences in Strings
#   In Python an another programming languages  \ followed by a character is an escape sequences.
#   Let us see the must common escape characters:

# \n: new line
# \t :Tab means(8 spaces)
# \\: Back slash
# \': Single quote
# \": Double quote

print('I hope everyone is enjoying the Python Challenge.\nAre you?')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash symbol (\\)')
print('In every programming language is starts with \"Hello, World!\"')


#   Old String Formatting 
#   %s - String (or any objects with a String representation, like numbers)
#   %d - Integers
#   %f - Floating point numbers
#   "%.number of digitsf" - Floating


#   Strings only

first_name = 'Lucathor'
last_name = 'Thorluca'
language = 'Python'
formated_string = 'I am %s %s. I tech %s' %(first_name, last_name, language)
print(formated_string)


#   String and numbers

radius = 10
pi = 3.14
area = pi * radius**2
formated_string ='The area of circle with a radius %d is %.2f.' %(radius, area)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string)


#   New style String formatting

first_name = 'Lucathor'
last_name = 'Thorluca'
language = 'Python'
formated_string = 'I am {} {}. I tech {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{}// {} = {}'.format(a, b, a //b))
print('{}** {} = {}'.format(a, b, a **b))



#   String and numbers

radius = 10
pi = 3.14
area = pi * radius**2
formated_string = 'The area of circle with a radius {} is {:.2f}.'. format(radius, area) # especifica 2 digitos de decimales
print(formated_string)


#   String interpolation / f-String (Python3.6+)

a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} //{b} = {a //b}')
print(f'{a} **{b} = {a **b}')



#   Python as sequences of characters

language = 'Python'
a,b,c,d,e,f = language # Desempaqueta los caracteres dentro de variables
print(a) # P → index 0
print(b) # y → index 1
print(c) # t → index 2
print(d) # h → index 3
print(e) # o → index 4
print(f) # n → index 5



# ↑  Accesing Characters in String by index   ↑
#    El index empieza desde "0", cero

language ='Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language)-1
print(last_index) # 5
last_letter = language[last_index]
print(last_letter)


# If we want start from right end we can use negative index. -1 is the last index

print('Here start from right')
language = 'Python'
last_index = language[-1]
print(last_index)
second_last = language[-2]
print(second_last)


#   Slicing Python String

language = 'Python'
first_three = language[0:3] # Comienza en el index 0 hasta el index 2. 
print(first_three)  #Pyt
last_three = language[3:6] # Las 3 ultimas posiciones
print(last_three)   # hon


# Anothers way
last_three = language[-3:]  # Indicando sólo el primer index, continua hasta el final de la secuencia
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon



#   Reversing a String

greeting = 'Hello,World!'
print(greeting[::-1])   #!dlroW olleH, lee desde el útlimo carácter hasta el primero


#   Skipping Characters while slicing
#   Omitir caracteres mientras se divide/corta

language = 'Python'
pto = language[0:6:2] 
# El 0 indica el primer caracter que se muestra
# El 6 indica el primer caracter que ya NO se muestra, el 5 es ultimo que se muestra
# El 2 es que va realizando saltos de 2 en dos. Solo muestra los que concidan con los saltos
print(pto)

print("\n__________________________________________________________________\n")
print("\n********************** BEGIN STRING METHODS **********************\n")
print("\n__________________________________________________________________\n")

# Capitalize() → Converts the first characters of the string to capital letter
print("\n************ Begin Capitalize method *************\n")

challenger = 'thirty days of python'
print(challenger.capitalize())  # Thirty days of python


# count() → Return occurrences of substring in string.
print("\n************ Begin count method *************\n")

challenge = 'thirty days of python'
print(challenge.count('y')) # 3, Muestra las veces que se repite el carácter
print(challenge.count('y', 7, 14)) # 1
    # La 'y' es el substring
    # El 7 es el comienzo
    # El 14 es el final
print(challenge.count('th'))    # 2


# endswith() → Checks if a string ends with a specified ending
print("\n************ Begin endswith method *************\n")

challenge = 'thirty days of python'
print(challenge.endswith('on'))     # True
print(challenge.endswith('tion'))   # False
print(challenge.endswith('thon'))   # True


# expandtabs() → Replaces tab character with spaces, default tab size is 8. It takes tab size argument
print("\n************ Begin expandtabs method *************\n")

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs())   #   8 spaces
print(challenge.expandtabs(10)) #   10 spaces


# find() →  Return the index of the first occurrence of a substring.
#           If not found returns -1
print("\n************ Begin find method *************\n")

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0


# rfind()  →  Return the index of last occurrence of a substring. If not found returns -1
print("\n************ Begin rfind method *************\n")

challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17


# format()  → formats string into a nicer output
print("************ Begin format method *************\n")

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314


#   index()  →  Returns the lowest index of a substring, additional arguments starting and eding index
#               (default 0 and string length -1). If the substring is not found it raises a valueError
print("\n************ Begin index method *************\n")

challenge = 'thirty days of python'
sub_string = 'da'       # substring que busca dentro del string challenge
print(challenge.index(sub_string))      # 7 ,   Devuelve el índice más alto de una subcadena


# rindex()  →  Returns the highest index of a substring 
print("\n************ Begin rindex method *************\n")

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))      # 7 ,   Devuelve el índice más bajo de una subcadena


# isalnum()  →  Checks alphanumeric character
print("\n************ Begin isalnum method *************\n")

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python' 
print(challenge.isalnum())  # False, space is not an alphanumeric character

challenge = 'thirty days of pyhton 2019'
print(challenge.isalnum())  # False, space is not an alphanumeric character


# isalpha()  →  Checks if all string elements are alphabet characters (a-z and A-Z)
print("\n************ Begin isalpha method *************\n")

challenge = 'thirty days of python'
print(challenge.isalpha())  # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())    # True
num = '123'
print(num.isalpha())  # False


#   isdecimal()  →  Checks if all characters are decimal (0-9)
print("\n************ Begin isdecimal method *************\n")

challenge = 'thirty days of python'
print(challenge.isdecimal())    # False
challenge = '123'
print(challenge.isdecimal())    # True
challenge = '\u00B2'
print(challenge.isdecimal())    # False
challenge = '12 3'
print(challenge.isdecimal())    # False, space not allowed
challenge = '12,1'
print(challenge.isdecimal())    # False



# isdigit()  →  Checks if all characters in a string are numbers (0-9 and some other unicode charcater for numbers)
print("\n************ Begin isdigit method *************\n")

challenge = 'Thirty'
print(challenge.isdigit())      # False
challenge = '30'
print(challenge.isdigit())      # True
challenge = '\u00B2'            # \u00B2 es un codigo unicode, representa elevado al cuadrado ▓
print(challenge.isdigit())      # True 
print('\u00B2')



# isnumeric() → Checks if all characters in a string are numbers or numbers related
#  (just like isdigit(). just accepts more symbols, like ½)
# Método integrado para el manejo de cadenas. Se usa para verificar si el argumento contiene 
# todos los caracteres numericos
print("\n************ Begin isnumeric method *************\n") 

num = '10'
print(num.isnumeric())      # True
num = '\u00BD'              # Codigo unicode que muestra ½ 
print(num.isnumeric())      # True
num = '10.5'
print(num.isnumeric())      # False, contiene un punto "10.5" que no se considera numerico



# isidentifier() → Checks for a valid identifier - it checks if a string a valid variale name
print("\n************ Begin isidentifier method *************\n") 
# Comprueba si es valido el nombre de la variable

challenge = '30DaysOfPython'
print(challenge.isidentifier())     # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())     # True



# islower → Checks if all alphabet character in the string are lowercase
print("\n************ Begin islower method *************\n") 

challenge = 'thirty days of python'
print(challenge.islower())              # True
challenge = 'Thisrty days of python'
print(challenge.islower())              # False


# isupper → Checks if all alphabet character in the string are uppercase
print("\n************ Begin isupper method *************\n")

challenge = 'thirty days of python'     # False
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())                # True


# join() → Returns a concatenated string
print("\n************ Begin join method *************\n")
# Convierte una lista en una cadena de texto teniendo que indicar que caracteres deseamos usar como delimitadores


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result)


# strip() Removes all given characters starting from the beginning and end of the string
print("\n************ Begin strip method *************\n")
# COMPARA LOS CARÁCTERES DE INICIO Y FIN con un conjunto de carácteres definidos por el usuario 
# y los elimina HASTA LLEGAR A UN CARACTER QUE NO COINCIDA, ES SENSIBLE CASE
#para eliminar caracteres solamente de la parte frontal o posterior de la misma, usa "lstrip()" (para el inicio de la cadena) y 
# "rstrip()" (para el final de la cadena)

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))      # 'irty days of py'
challenge = 'estol es seunaes pruebato personalestes'
print(challenge.strip('estl'))        # tol es seunaes pruebato personal



# replace() → Replaces substring with a given string
print("\n************ Begin replace method *************\n")
# Sustituye el primer argumento que existe en el string, por el segundo argumento dado

challenge = 'thirty days of python'
print(challenge.replace('of python', 'your coding'))        # thirty days of coding


# split() → Split the string, using given string or space as a separator
print("\n************ Begin split method *************\n")
# Divide una cadena y devuelve una lista de subcadenas

challenge = 'thirty days of python'
print(challenge.split())        # ['thirty', 'days', 'of', 'python'] → Lista de substring que devuelve el metodo split
challenge = 'thirty, days, of, python'
print(challenge.split(', '))    # ['thirty', 'days', 'of', 'python']


# title() → Returns a title cased string
print("\n************ Begin title method *************\n")

challenge = 'thirty days of python'
print(challenge.title())        # Thirty Days Of Python


# swapcase() → Converts all characters uppercase to lowercase and all lowercase characters to uppercase characters
print("\n************ Begin swapcase method *************\n")

challenge = 'thirty days of python'
print(challenge.swapcase())     # chance to uppercase → THIRTY DAYS OF PYTHON
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.swapcase())     # chance to lowercase → thirty days of python


# startswith() → Checks if String with the Specified String
print("\n************ Begin startswith method *************\n")

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))       # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))       # False
challenge = '30 days of python'
print(challenge.startswith('30'))           # True


# 












