print("[---------------------<>TUPLES<>---------------------]")

# A tuple is a collection of different data types which is ordered and inmutable.
# Once created we cannot changes its values. We cannot use append, insert and remove.

# Syntax
# empty_tuple = ()
# empty_tuple = tuple() → Using the tuple constructor

# Syntax with initial values
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuple length

print(tpl)
print(len(tpl))

# Accesing tuple items
# With positive index start by 0
first_item = tpl[0]
print("The first item in the list tpl is ",first_item)    # item1
second_item = tpl[1]
print("The second item in the list tpl is ",second_item)    # item2


# Negative indexing means beginning from the end (-1)
last_item = tpl[-1]
second_last = tpl[-2]
print("The last item is", last_item, "and the second last is", second_last)


print("\n[--------------------------< > SLICING < >--------------------------]\n")

# We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple
# the return value will be a new tuple with the specified items


# Range of Positive indexes
# Syntax
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]    # all items
print(all_items)
all_items = tpl[:4]     # all items
print(all_items)
all_items = tpl[0:]     # all items
print(all_items)
middle_two_items = tpl[1:3]     # Not included items in index0 and index3
print(middle_two_items)


fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)
all_fruits = fruits[0:4]    # all items
print(all_fruits)
all_fruits = fruits[0:]     # all items
print(all_fruits)
orange_mango = fruits[1:3]  # orange and mango
print("orange and mango", orange_mango)
orange_to_the_rest = fruits[1:]
print("The rest", orange_to_the_rest)



# Range of the negative indexes

all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]    # orange and mango
orange_to_the_rest = fruits[-3:]



print("\n[---------------< > CHANGING TUPLES TO LISTS < >-------------------]\n")

# We can change tuples to lists and lists to tuples. Tuples is inmutable 
# if want to modify a tuple we should change it to a list

# Syntax
# tpl = ('item1', 'item2', 'item3', 'item4')
# lst = list(tpl)

# example
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)
print(fruits)

#Example 2

prueba = ('uno', 'dos', 'tres', 'cuatro')
prueba = list(prueba)
prueba[0] = 'zero'
print(prueba)
prueba = tuple(prueba)
print(prueba)


# Checking an item in a tuple, if an item exist or not, it returns a boolean

#Syntax
tpl  = ('item1', 'item2', 'item3', 'item4')
print('item2' in tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)

# Joining tuples
#Syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2

# Example
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
print(fruits + vegetables)


# Deleting Tuples
#Syntax

tpl1 = ('item1', 'item2', 'item3')
del tpl1
