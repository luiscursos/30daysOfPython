print ("\n***********************  EXERCISES DAY 4  ***********************\n")


# 1 → Concatenate the string  'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
print("\n__________________Exercises 1__________________\n")

string = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(string)
print(result)


# 2 → Concatenate the string  'Coding', 'For' , 'All' for all to a single string "Coding For All"
print("\n__________________Exercises 2__________________\n")

challenge2 = 'Coding', 'For' , 'All'
result2 = ' '.join(challenge2)
print(result2)


# 3 → Declare a variable named company and assign it to an ainitial value "Coding For All"
print("\n__________________Exercises 3__________________\n")

company = "Coding For All"


# 4 → Print variable
print("\n__________________Exercises 4__________________\n")

print(company)


# 5 → Print the length of the company string using len() method and print
print("\n__________________Exercises 5__________________\n")

print(len(company))


# 6 → Change all the characters to lowercase letters using upper() method
print("\n__________________Exercises 6__________________\n")

print(company.upper())


# 7 → Change all the characters to lowercase letters using lower() method
print("\n__________________Exercises 7__________________\n")

print(company.lower())


# 8 → Use capitalize(), title(), swapcase(), methods to format the value of the string Coding For All
print("\n__________________Exercises 8__________________\n")

challenge8 = 'Coding For All'
print(challenge8.capitalize())
print(challenge8.title())
print(challenge8.swapcase())


# 9 → Cut (slice) out the first word of Coding For All string. (Cortar la primera palabra de la cadena)
print("\n__________________Exercises 9__________________\n")

challenge9 = 'Coding For All'
result9 = challenge9[6:]
print(result9)


# 10 → Check if Coding For All string conains a word Coding using the method index. fin dor other method
print("\n__________________Exercises 10__________________\n")

challenge10 = 'Coding For All'
sub_string10 = 'Coding'
print(challenge10.index(sub_string10))
print(challenge10.find('Coding'))


# 11 → Replace the word coding in the string 'Coding For All' to Python
print("\n__________________Exercises 11__________________\n")

challenge11 = 'Coding For All'
print(challenge10.replace('Coding','Python'))


# 12 → Change Python for Everyone to Python for All using the replace method or other methods
print("\n__________________Exercises 12__________________\n")

challenge12 = 'Python for Everyone'
print(challenge12.replace('Everyone', 'All'))


# 13 → Split the string 'Coding For All' using space as the separator
print("\n__________________Exercises 13__________________\n")

challenge13 = 'Coding For All'
print(challenge13.split(' '))
print(challenge13.split())          # split usa un separador y con valor -1 de maxsplit por defecto
print(challenge13.split(sep= ' '))
print(challenge13.split(sep=None, maxsplit=-1))


# 14 → "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
print("\n__________________Exercises 14__________________\n")

challenge14 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(challenge14.split())          # MAL, De este modo se realiza split en el espacio manteniendo duplicando la coma
print(challenge14.split(','))       # BIEN, El split se realiza justo donde se encuentra la coma


# 15 → What is the character at index 0 in the string Coding For All
print("\n__________________Exercises 15__________________\n")

challenge15 = 'Coding For All'
print("The first index is ",challenge15[0])


# 16 → What is the last index at the string Coding For All
print("\n__________________Exercises 16__________________\n")

challenge16 = 'Coding For All'
print("The last index is ",challenge16[-1])


# 17 → What character is at index 10 in "Coding For All" string
print("\n__________________Exercises 17__________________\n")

challenge17 = 'Coding For All'
print("The character at index 10 is ", challenge17[10] , "← one space")


# 18 → Create an acronym or an abbreviation for the name 'Python For Everyone'
print("\n__________________Exercises 18__________________\n")

challenge18 = 'Python For Everyone'     #PyFE
acronym18=(challenge18[0:2])+(challenge18[7:9])+(challenge18[11:13])
print(acronym18)        # PyFoEv, las 2 primeras letras de cada palabra


# 19 → Create an acronnym or an abbreviation for the name 'Coding For All' string.
print("\n__________________Exercises 19__________________\n")

challenge19 = 'Coding For All'
acronym19 = (challenge19[0:1])+(challenge19[7:9])+(challenge19[11:13])
print(acronym19)        # CFoAl, las 2 primeras letras de cada palabra


# 20 → Use index to determinate the position of the first occurrence of C in Coding For All
print("\n__________________Exercises 20__________________\n")

challenge20 = 'Coding For All'
print(challenge20.index('C'))


# 21 → Use index to determinate the position of the first occurrence of F in Coding For All
print("\n__________________Exercises 21__________________\n")

challenge21 = 'Coding For All'
print(challenge21.index('F'))


# 22 → Use index to determinate the position of the first occurrence of F in Coding For All
print("\n__________________Exercises 22__________________\n")

challenge22 = 'Coding For All'
print(challenge22.index('l'))


# 23 → Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# "You cannot end a sentence with because because because is a conjunction".
print("\n__________________Exercises 23__________________\n")

challenge23 = 'You cannot end a sentence with because because because is a conjunction'
print(challenge23.index('because'))     # 31


# 24 → Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print("\n__________________Exercises 24__________________\n")

challenge24 = 'You cannot end a sentence with because because because is a conjunction'
print(challenge24.rindex('because'))


# 25 → Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print("\n__________________Exercises 25__________________\n")

challenge25 = 'You cannot end a sentence with because because because is a conjunction'
result25=(challenge25[0:31])+(challenge25[54::])
print(result25)
print(challenge25.index('because'))
print(challenge25.rindex('because'))


# 26 → Find the position of the first occurrence of the word 'because' in the following sentence:
#      "You cannot end a sentence with because because because is a conjunction"
print("\n__________________Exercises 26__________________\n")

challenge26 = "You cannot end a sentence with because because because is a conjunction"
print(challenge26.find('because'))


# 27 → Slice out the phrase 'because because because' in the following sentences:
#      "You cannot end a sentence with because because because is a conjunction"
print("\n__________________Exercises 27__________________\n")

challenge27 = 'You cannot end a sentence with because because because is a conjunction'
result27=(challenge27[0:31])+(challenge27[54::])
print(result27)


# 28 → Does "Coding For All" start with a substring Coding?
print("\n__________________Exercises 28__________________\n")

challenge28 = 'Coding For All'
print(challenge28.startswith('Coding'))     # True


# 29 → Does 'Coding For All' end with a substring coding?
print("\n__________________Exercises 29__________________\n")

challenge29 = 'Coding For All'
print(challenge29.endswith('coding'))


# 30 → ' Coding For All ', remove the left and right trailing spaces in the given string (Eliminas espacios finales izquierdo y derecho)
print("\n__________________Exercises 30__________________\n")

challenge30 = ' Coding For All '
print(challenge30[1:-1])        # Mostramos desde el index 1 al -2


# 31 → Which one of the following variables return True when we use the method isidentifier()
        # 30DaysOfPython
        # thirty_days_of_python
print("\n__________________Exercises 31__________________\n")

challenge31a = '30DaysOfPython'
challenge31b = 'thirty_days_of_python'
print(challenge31a.isidentifier())
print(challenge31b.isidentifier())


# 32 → The following list contains the names of some of python libraries:['Django','Flask','Bottle','Pyramid','Falcon']
#      Join the list with a hash with space string
print("\n__________________Exercises 31__________________\n")

challenge33 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result33 = '#'.join(challenge33)
print(result33)


# 33 → Use the new line escape sequence to separate the following sentences.
print("\n__________________Exercises 33__________________\n")

challenge33a = 'I am enjoying... \n...this challenge'
challenge33b = 'I just wonder... \n...what is next'
print(challenge33a)
print(challenge33b) 


# 34 →  Use a tab escape sequence to write the following lines
print("\n__________________Exercises 34__________________\n")

print('''
Name    \tAge\tCountry\tCity
Asabeneh\t250\tFinland\tHelsinki
''')


# 35 → Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
print("\n__________________Exercises 35__________________\n")

radius = 10
area = 3.14 * radius **2
formated_string  = ('The area of a circle with radius {} is {:.2f} meters square').format(radius, area)
print(formated_string)


# 36 → Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

print("\n__________________Exercises 36__________________\n")

a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} //{b} = {a //b}')
print(f'{a} **{b} = {a **b}')







