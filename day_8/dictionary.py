
# Creating a Dictionary
# To create a dictionary we used a curly brackets{} or the dict() build-in function

# Syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 'key5':'value5'}


# Example
# The dictionary could be any data types: string, boolean, list, tuples, set or a dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':False,
    'skills':['JavaScript','React','node','MongoDB','Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}


# Dictionary length
# It checks the number of 'key: value' pairs in the dictionary

# Syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct))

# Example
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{'street':'Space street',
    'zipcode':'02210'}
}
print(len(person))


# ACCESING DICTIONARY ITEMS
#   We can access Dictionary items by referring to its key name

#Syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1'])   # value1
print(dct['key2'])   # value2

# Example

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'is_married':False,
    'country':'Finland',
    'skills':['JavaScript','React','Node', 'MongoDB', 'Python'],
    'address':{
        'street':'space street',
        'zipcode':'02210'}

}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['is_married'])
print(person['country'])
print(person['skills'])
print(person['address'])



# Si la key no existe se lanzara un error, Para comprobar si existe podemos usar el método get
# El metodo get devuelve None si el objeto, la key no existe


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'is_married':False,
    'country':'Finland',
    'skills':['JavaScript','React','Node','MongoDB','Python'],
    'address':{
        'street':'space street',
        'zipcode':'02210'
    }
}

print(person.get('first_name'))
print(person.get('last_name'))
print(person.get('age'))
print(person.get('is_married'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('address'))
print(person.get('city'))       # Return none, doesn't exist this key



# Adding items to a dictionary
# We can add new key and value pairs to a dictionary

# Syntax
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
dct['key5']='value5'        # Add a new key and value pairs
print(dct)


# Example

person ={
    'first_name':'lucathor',
    'last_name':'thorluca',
    'age':124,
    'is_married':False,
    'country':'Finland',
    'skills':['JavaScript','React','Node','MongoDB','Python'],
    'address':{
        'street':'space street',
        'zipcode':'09872'
    }
}

person['state']='Spain'
person['skills'].append('HTML')
print(person)



# Modifying items in a dictionary
# We can modify items in a dictionary

# Syntax
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
dct['key1']='value-one'     # Modifying the value in key1
print(dct)      # {'key1': 'value-one', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}


# Checking keys in a dictionary
# We use the operator 'in' to check if a key exist in a dictionary

# Syntax
dct = {'key1':'value1','key2':'value2', 'key3':'value3','key4':'value4'}
print('key2' in dct)    # True
print('key5' in dct)    # False


# Removing key and value pairs from a dictionary

    # pop(key) : removes the item with the specified key name
    # popitem() : remove the last item
    # del : removes an item with specified key name

# Syntax
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
dct.pop('key1')     # removes key item
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
dct.popitem()       # remove the last item
del dct['key2']     # remove key2 item
print(dct)


# Example

person = {
    'first_name':'lucathor',
    'last_name':'thorluca',
    'age':127,
    'is_married':False,
    'country':'Finland',
    'skills':['JavaScript','React','Node','MongoDB','Python','HTML'],
    'address':{
        'street':'space street',
        'zipcode':'021023'}
}

person.pop('first_name')        # Removes the firstname item
person.popitem()                # Remove the last item
del person['is_married']        # Remove the is_married item

print(person)


#  Changing dictionary to a list of items
# The items() method changes dictionary to a list of tuples

# Syntax
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
print(dct.items())      # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])


# Clearing a dictionary
# Syntax
print(dct.clear())      # none  
print(dct)


# Copy in a dictionary
# We can copy a dictionary using copy method. Using copy we can avoid mutation of the original dictionary
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])



# Getting dictionary values as a list
# The values method gives us all the values of a dictionary as a list
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
values = dct.values()
print(values)       # dict_values(['value1', 'value2', 'value3', 'value4'])