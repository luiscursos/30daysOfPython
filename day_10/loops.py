print ("\n***********************  EXERCISES DAY 10  ***********************\n")


print("\n[_______________________________LOOPS_______________________________]\n")

'''
Two looops
    1- while -> Se ejecutará mientras la condición resulte True
    2- for   -> 



'''
### While ###

count = 0   
while count < 5:    # La condición se vuelve falsa cuando la variable count tiene como valor 5
    print(count)
    count = count + 1

# Podemos usar un else cuando la condición del bloque while se vuelva falsa

count = 0
while count < 5:
    print(count)
    count = count + 1
else:               # El else se ejecuta cuando la condición se vuelve False
    print(count)


# Break and Continue - Part 1

# We use break when we like to get out of or stop the loop

count = 0

while count < 5:
    print("Exercises of break",count)
    count +=1
    if count == 3:
        break


# With the continue statement we can skip the current iteration, and continue with the next

count = 0

while count < 5:
    count +=1
    if count == 3:
        continue
    print(count)





print("\nFor Loop\n")
# Is used for iterating over a sequence (thats is either a list, a tuple, a dictionary, a set or a string)

numbers = [0, 1, 2, 3, 4, 5]

for number in numbers:
    print(number)

language = 'Python'
for letter in language:
    print("letter",letter)

for i in range(len(language)):
    print("range",language[i])

    
    
    # For loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# Looping through a dictionary gives to the key of the dictionary

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

#Loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in it_companies:
    print(company)




#Break and Continue - Part2

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number ==3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be', number+1)
    if number != 5: 
        print("it's not five")
    else:
        print("loop's end")


## The range function ##

# Is used list of numbers. The range(start,end, step) takes three parameters.
#By default it start from 0' and the increment is 1.
# Needs at least 1 argument (necesita al menos un argumento)

lst = list(range(11))
print(lst)
st = set(range(11))
print(st)

lst = list(range(0,11,2))
print(lst)
st = set(range(0,11,2))
print(st)

for i in range(20,-10, -2):     # range inverso
    print("The last range" , i)


# Nested for loop (Bucle anidado)
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
## Iterar con un bucle anindado sobre una lista dentro de un dict

for key in person:
    if key == "skills":
        for skill in person['skills']:
            print(skill)
            


# For else

for number in range(11):
    print(number)
else:
    print("The loop stop at")


# Pass

for number in range(6):
    pass    # Evita errores al no incluir ninguna declaracion dentro del bucle for


