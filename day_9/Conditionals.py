
# IF CONDITION

# The key word «if» is user to check if a condition is true and to execute the block code
# Remember the identation afer the colon (dos puntos :).
# if condition:
#     this part of code runs of truthy conditiions

# Example 1

a = 3
if a > 0:
    print('A is a positive number')



# IF ELSE
# If condition is true the first block will be executed, if not the else condition will run

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')


# IF ELIF ELSE
# We use «elif» when we have multiple conditions

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')


# Short hand
# Syntax
# code if condition else code

# Example

a = 3
print('A is positive') if a > 0 else print('A is negative')


# Nested Conditions (Condiciones anidadas)
# Conditions can be nested
# We can writting nested condition by using the logical operator «and»
# Example

a = 1
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


# Example

a = 10
if a > 0 and a % 2 == 0:
    print('A is a positive and even integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative integer')



# «IF» AND «OR» LOGICAL OPERATOR

# Example

user = 'admin'
access_level = 4
if user == 'admin' or access_level >= 4:
    print('access granted!')
else:
    print('Access Denied!')