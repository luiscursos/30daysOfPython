from gettext import find


print("[____________________________FUNCTIONS_____________________________________")

# Declaring a function
def function_name():
    print("code block")

# Invoking/Calling a function
function_name()

# printing the result function
print(function_name)

# Function can be declared without parameters

def generated_full_name():
    first_name = 'Lu'
    last_name = 'Cathor'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name) # Al tener print y no return devolvera el valor de full_name y también None

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one+num_two
    return(total)

print(generated_full_name())
print(add_two_numbers())


# Function with parameters

# We can different data types \
# (number, string, boolean, list, tuple, dictionary or set)
# if our functions takes a perameter we should call our function with an argument

def function_name (parameter):
    return("code_block")

print(function_name("argument"))

def greetings (name):
    message = name + ', welcome to Python for Everyone'
    return message

print(greetings('Lucathor'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x*x
print(square_number(2))

def area_of_circle(r):
    PI = 3.14
    area = PI * r**2
    return area
print("The area is ",area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(5)) # 15 → 1+2+3+4+5
print(sum_of_numbers(10)) # 55 → 1+2+3+4+5+6+7+8+9+10

#Two parameters
def sum_two_parameters (first_parameters, second_parameters):
    return first_parameters + second_parameters

print(sum_two_parameters(21, 26))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print(calculate_age(2022, 1982))


def weight_of_object (mass, gravity):
    weight = (mass*gravity), ' N' # the value has to be changed to a string first
    return weight

print('Weight of an object in Newtons: ', weight_of_object(100, 981))


# Passing arguments with key and value
# The order arguments does not matter


def print_fullname(firstname, lastname):
    fullname = firstname + ' ' + lastname
    return fullname

print(print_fullname(lastname='cathor', firstname='lu'))


# Returing a boolean

def is_even (n):
    if n%2 == 0:
        print('even')
        return True
    else:
        return False

print(is_even(4))   # True
print(is_even(13))  # False

#  Returing a list
# Define una lista con numeros pares

def find_even_number(n):    
    evens = []
    for i in range (n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(find_even_number(123))


# Function with default parameters
# If we do not pass argument when calling the function, 
# their default values will be used

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Lucathor'))


def generate_full_name (first_name = 'Lu', last_name = 'Cathor'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('Luis', 'Camacho'))


def calculate_age(birth_year,current_year = 2022):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(1982))

def weight_of_an_object(mass, gravity = 9.81):
    weight = (mass*gravity), ' N'
    return weight

print('Weight of an object in Newtons: ', weight_of_an_object(100)) # 9.81 → Average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_an_object(100,1.62)) # gravity on the surface of the Moon


# Arbitrary number of arguments
# If we not know the number of arguments, we can adding * before the paameter name
# the same as unpacking


def sum_all_nums (*nums):
    total = 0
    for num in nums: 
        total += num
    return total

print(sum_all_nums(2, 3, 5))    # 10


# DEafault and arbitrary number of parameters 

def generate_groups(team, *args):
    print(team)
    for i in args:  # itera sobre la tupla que se le pasa en la llamada
        print(i)

print(generate_groups('Team-1', 'Luacthor', 'Brooks', 'Jason', 'Eyob'))


# Function as parameter of another function
# You can pass function around as parameter

def square_number (n):
    return n*n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))
