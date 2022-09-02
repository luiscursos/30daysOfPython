# There are four collection data types


    #   lists : 
        #   ordered
        #   mutable
        #   Allows duplicate members


    #   Tuple:
        #   ordered
        #   inmutable
        #   Allows duplicate members
    

    #   Set:
        #   Unordered 
        #   un-indexed
        #   inmutable
        #   permit add new items
        #   Allows duplicate members  


    #   Dictionary:
        #   is Unordered
        #   mutable
        #   indexed
        #   No duplicate members



#   A list is a collection of different data types which is ordered and modifiable(mutable)
#   A list can be empty or it may have different data type items


# Using list built-in function
# Syntax
lst = list()            # Create list with built-in function
empty_list = list()     # This is an empty list, no item in the list
print(len(empty_list))  


# Using square brackets, []
# sintax
lst = []            # Create list

empty_list = []     # This is an empty list, no item in the list
print(len(empty_list))


# list with initial vlaues. We use len() to find the length of a list

fruits = ['banana', 'orange', 'mango', 'lemon']                                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']                     # list of vegetables
animal_products = ['milk', 'meat', 'butter' , 'yoghurt']                            # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']     # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']


print('fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of Animal products:', len(animal_products))
print('Web Techs:', web_techs)
print('Number of Web Techs:', len(web_techs))
print('Countries:', countries)
print('Numbers of countries:', len(countries))


# list can have items of different data types
lst = ['Asabenech', 250, True, {'country':'Finland', 'city':'Helsinky'}]
print(lst)


# Accessing list items using POSITIVE INDEX
    #    fruits = ['banana', 'orange', 'mango', 'lemon']
    #     index →      0         1        2        3              
# We access each item in a list using their index. A list index start from 0

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)

# last index
last_index = len(fruits)-1
last_fruit = fruits[last_index]


# Accessing list items Using NEGATIVE INDEX
# Negative indexing means beginning from the end, 
        # -1 refers to the last  item, 
        # -2 referes to the second last item


    #    fruits = ['banana', 'orange', 'mango', 'lemon']
    #     index →      -4       -3       -2      -1


fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)          # banana 
print(last_fruit)           # lemon
print(second_last)          # mango


# ****************** UNPACKING LIST ITEMS ******************

# La variable que este predecedidad por el simbolo * , almacenara todas las variables restantes
# La variable *rest, no tiene porque ser la ultima, ya que podemos incluir detras de ella

lst = ['item', 'item2', 'item3', 'item4', 'item5']      
first_item, second_item, third_item, *rest = lst        
                                                        
print(first_item)       # primer item de la lista
print(second_item)      # segundo item de la lista
print(third_item)       # tercer item de la lista
print(rest)             # el resto de items de la lista que no disponen de variebl


# First example

lst = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *resto = lst

print(first_fruit)
print(second_fruit)
print(third_fruit)
print(resto)

# Second example about unpacking list

first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)        # 1
print(second)       # 2
print(third)        # 3
print(rest)         # [4, 5, 6, 7, 8, 9]
print(tenth)        # 10


# Third example about unpacking list

countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)


# ****************** SLICING ITEMS FROM A LIST ****************** 


# Positive indexing: 
            #  We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list
    
    # Default values:
        # start = 0
        # end = len(lst) -1 (last item) 
        # step = 1  


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
print(all_fruits)           # Its returns all the fruits
all_fruits = fruits[0:]
print(all_fruits)                   # Its returns all the fruits

orange_and_mango = fruits[1:3]
print(orange_and_mango)             # ['orange', 'mango']

orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)           # ['orange', 'mango', 'lemon']

orange_lemon = fruits[::2]      
print(orange_lemon)                 # ['banana', 'mango']



# Negative indexing: 
        # We can specify a range of negative indexes by specifying the start, end and step, the return values will be a new list.

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]        # It returns all the fruits
print(all_fruits)
print('what',fruits[-1:])       # lemon

orange_and_mango = fruits[-3:-1]
print(orange_and_mango)         # ['orange', 'mango']   

orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)       # ['orange', 'mango', 'lemon']

reverse_fruit = fruits[::-1]
print(reverse_fruit)            # ['lemon', 'mango', 'orange', 'banana']


# Modifying list

# list is a mutable or modifiable ordered collection of items. Lets modify the fruit list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado' # Aguacate
print(fruits)       #   ['banana', 'orange', 'mango', 'lemon']

fruits[1] = 'apple'
print(fruits)       #   ['avocado', 'apple', 'mango', 'lemon']

last_index = len(fruits) -1
fruits[last_index] = 'lime'
print(fruits)       #   ['avocado', 'apple', 'mango', 'lime']


#   Checking item in a list

# Checking an item if it is a member of a list using in operator. See the example below
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)


#   Adding Items to a list
# To add item to the end of an existing list we use the method append()
# Agregar elemento al final aumentando la cantidad de item en lista
#   sintax
        # lst = list()
        # lst.append('item')      # Agrega 'item' como último elemento de la lista
        # print(lst)


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']



# Inserting Items into a List

# We can use insert() method to insert a single item item at a specified index in a list.
# The other items are shifted to the right.
# The insert() method takes two arguments: index and an item to insert

# sintax

        # lst = ['item1', 'item2']
        # lst.insert(index, item)


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2,'apple')
print(fruits)

fruits.insert(3, 'lime')
print(fruits)


#   Removing items from a list

# The remove method removes a specified item from a list

#   Syntax
        # lst = ['item', 'item']
        # lst.remove(item)


fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')     # This method removes the first occurrence of the item in the list
print(fruits)
fruits.remove('lemon')
print(fruits)


#   Removing items Using Pop
#   The Pop() method removes the specified index, (or the last item if index is not specified)

# Sintax
        # lst = ['item1', 'item2']
        # lst.pop()      # last item
        # lst.pop(index)

print("**************Pop Method************")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']
fruits.pop(0)
print(fruits)       # ['orange', 'mango']

print("**************del Method***********")
#   Removing item Using Del
# The del keyword removes the specified index and it can also be used to delete items within index range.
#   It can also delete the list completely

#   Sintax
        # lst = ['item1', 'item2']
        # del lst[index]      only a single item
        # del lst             to delete the list completely

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange','lemon', 'kiwi', 'lime']
del fruits[1:3]      # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits          # delete the list



#   Clering list items
#   The clear() method empties the list

#   sintax

        # lst = ['item1', 'item2']
        # lst.clear()


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)


# Copying a List
# sintax

lst = ['item1', 'item2']
lst_copy = lst.copy()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)


# Joining List

# There are several way to join, or concatenate two or more lists
        # Plus Operator (+)

# sintax
        # list3 = list1 + list2

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vgetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)


# Joining using extend() method The extend() method allows to append list ina list.

# sintax
        # list1 = ['item1', 'item2']
        # list2 = ['item3', 'item4']
        # list1.extend(list2)
        # print(list1)
        # print(list2)


num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers: ',num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers: ', negative_numbers)           # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables: ', fruits)        # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']


# Counting items in a list
#   The count() method returns the number of times an item appears in a list

# sintax
        # lst = ['item1', 'item2']
        # lst.count(item)


fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("The item 24 appears", ages.count(24), "times")   # 'The 24 item appears 3 times


#   Find index of an item

# the index() method returns the index of an item in the list:

# syntax
        # lst = ['item1', 'item2']
        # lst.index[item]

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("The index of 24 item is", ages.count(24))        # The index of 24 item is 3


# Reversing a List

# The reverse method reverses the order of a list

# syntax
        # lst = ['item1', 'item2']
        # lst.reverse()


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()        
print(fruits)           # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)     # [24, 25, 24, 26, 25, 24, 19, 22]



#   Sorting List items

# To sort lists we can use sort() method or sorted() built-in functions. 
# The sort() method reorders the list items in ascending order and modifies the original list
# If an argument of sort() method  " reverse = True ", it will arrange the list in descending order.

# syntax
        # lst = ['item1', 'item2']
        # lst.sort()                  # Ascending
        # lst.sort(reverse=True)      # Descending


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()                   # Ascending
print(fruits)                   # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)       # Descending
print(fruits)                   # ['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)         #  [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)
print(ages)         #  [26, 25, 25, 24, 24, 24, 22, 19]



# Sorte(): returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print("The order with sorted method is", sorted(fruits))           # ['banana', 'lemon', 'mango', 'orange']

#Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print("No modify the original list", fruits)    #       ['orange', 'mango', 'lemon', 'banana']
print("The reverse=true order with sorted method is", sorted(fruits,reverse=True))           # ['orange', 'mango', 'lemon', 'banana']


