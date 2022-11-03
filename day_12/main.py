import mymodule



print(mymodule.generate_full_name('Luis', 'Camacho'))

# Import Functions from a Module
# We can have a many functions in a file.

from mymodule import generate_full_name, sum_two_nums, weight_of_object
print(generate_full_name("Luis", "Camacho"))
print(sum_two_nums(1,9))
print (weight_of_object(100,52))
#print(person["firstname"])


# During importing we can rename a name of the module

from mymodule import generate_full_name as fullname, sum_two_nums as total
print(fullname("Luca", "Thor"))
print(total(1, 9))
gravity=1
mass = 100
weight = mass * gravity
print(weight)


# import built-in modules
# The OS Module in Python provides function for creating, changing current working directory, 
# and removing a directory(folder), fetching its contents, changing and 
# identifying the current directory

# import the module
import os
# Creating directory
os.mkdir('test_os_module')
# Changing the current directory
os.chdir('.')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir('test_os_module')