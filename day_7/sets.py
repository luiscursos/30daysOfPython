
print("[____________________________SETS_____________________________________")



# Set es una colección de elementos que:
            # Es desordenada con elementos que no se repiten
            # Es mutable
            # Diferentes tipos de datos
            # Elementos mezclables, su hashable no cambia

# Creating a Set
# We use curly brackets, {} to create a set or the set{} buil_in_function

#Creating a empty set
#Syntax

st = {}
st = set()

# Creating a set with initial items
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'item1', 'item2', 'item3', 'item4'}

# Getting set's length
print(len(st))


# We use loops to access items. We will see this in loop section
 
 # Checking an item
# To check if an item exist in a list we use in membership operator (in)
print('item1' in st)        # True


# Add items to a Set
# Once a ser is created we cannot change any items and we can also add additional items
# Add one item using add()

# Syntax
st.add('item5')     # Add one item to a set
print(st)

# Add multiple items using update()
# The update() allows to add multiple items to a set.
# The update() take a list argument

# Example1
st.update(['item5', 'item6', 'item7'])      # Add more than one item to a set
print(st)

# Example2
fruits = {'bananas','orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)       # Join the fruits and vegetables sets
print(fruits)


# Removing items from a Set with remove() method
st.remove('item1')
fruits.remove('lemon')      # Remove the lemon item
print(fruits)


# The pop() method remove a random item from a list and it returns the remove item
# El método pop() elimina un elemento aleatoriamente
remove_item = fruits.pop()      # Almacenar el item removido aleatoriamente en una variable
print(remove_item)
print(fruits)


# Clearing items in a Set
# If we want to clear or empty the set we use clear method

# Syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear        # We empty list
print(fruits)


# Deleting a set
del st
del fruits


# Converting list to set
# We can convert list to set and set to list. 
# Converting list to set removes duplicates and only unique items will be reserved
# Syntax

lst = ['item1', 'item2', 'item3', 'item1']
print("lista",lst)      #   ['item1', 'item2', 'item3', 'item1']
st = set(lst)
print("set",st)         #   {'item1', 'item3', 'item2'}


#   Joining Sets
# We can join two sets using the union() or update()method
# Union This method returns a new set

# Syntax union method
st1 = {'item1', 'item2', 'item3', 'item4'}
print("st1", st1)
st2 = {'item5', 'item6', 'item7', 'item8', 'item1'}
print("st2", st2)
st3 = st1.union(st2)
print("st3 method union",st3) 

# Syntax update method

st1 = {'item1', 'item2', 'item3', 'item4'}
print("st1", st1)
st2 = {'item5', 'item6', 'item7', 'item8'}
print()
st1.update(st2)
print(st1)


# Finding intersection items
# Intersection returns a set of items which are in both the sets.
# Syntax

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item4'}
st3={}
st3 = st1.intersection(st2)
print("st3 inersection method", st3)    #   {'item4', 'item2'}


# Example
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print("The whole numbers",whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.intersection(dragon))      #   {'o', 'n'}


#   Cheking Subset and Super set

# A set can be a subset or super set  of the other set
    # Subset:issubset()
    # Super set: issuperset


# Syntax

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print("Checking subset: ",st2.issubset(st1))        # True, Comprueba si set2 dado es subconjunto de set1
print("Checking superset:",st1.issuperset(st2))     # True, Comprueba si set1 dado es un superconjunto de set2


# Checking the difference between two sets
# It returns the difference

# Syntax
st1 = {'item1', 'item2', 'item3', 'item4'} 
st2 = {'item2', 'item3'}
print("Difference between st2 vs st1",st2.difference(st1))  # set(), No muestra diferencia porque los 2 items de st2 se encuentran en st1
print("Difference between st1 vs st2",st1.difference(st2))  #{'item4', 'item1'}



#   Finding Symmetric Difference Between two sets

#   It returns the symmetric difference between two sets. 
#   It means that it returns a set that contains all items from both sets
#   except items that are present in the both sets, mthematically: (A\B) ∪ (B\A)
#   El símbolo unicode ∪ , significa union. 
#   El símbolo unicode ∩ representa intersección

# Syntax 

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
print("symmetric difference: ",st2.symmetric_difference(st1))    # {'item1', 'item4'}
print("symmetric difference: ",st1.symmetric_difference(st2))    # {'item1', 'item4'}


# Example

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print("Example symmetric difference: ", whole_numbers.symmetric_difference(some_numbers))   # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print("The symmetric difference method is:", python.symmetric_difference(dragon))   # {'h', 'r', 'p', 't', 'd', 'y', 'a', 'g'}


#   Joining sets

# If two sets do not have a common item or items we call them disjoint sets.
# We can check if two sets are join or disjoint using isdisjoint() method

# Syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print("isdisjoint method ", st1.isdisjoint(st2))    # False, Asi sabemos si los sets tienen items en común o no.


# Example2

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print("Example2 isdisjoint method", even_numbers.isdisjoint(odd_numbers))   # True


