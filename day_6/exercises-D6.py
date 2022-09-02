print("[_______________________________EXERCISES LEVEL 1_______________________________]")

# 1 - Create an empty tuple
empty_tpl  = ()

# 2 - Create a tuple containing names of your brothers 
marvel = ('Thor', 'Iron Man', 'Spyderman', 'Ant-Man')
marvela = ('Viuda Negra', 'Capitana Marvel', 'Wonder Woman')

# 3 - Join brothers and sisters tuples and assign it to siblings
siblings = marvel + marvela
print(siblings)

# 4 - How many siblings do you have
print(len(siblings))

# 5 - Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings[0] = 'Super Lopez'
siblings[-1] = 'Mortadelo'
siblings[4] = 'Filemon'
family_members = tuple(siblings)
print(family_members)


print("[_______________________________EXERCISES LEVEL 2_______________________________]")

# 1 - Unpack siblings and parents from family_members
br, sys, pet, *rest = siblings
print(rest)

# 2 - Create fruits, vegetables and animal products tuples. 
# Join the three and assign it to a variable called food_stuff_tp

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetable = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter' , 'yoghurt')

food_stuff_tp = fruits + vegetable + animal_products


# 3 - Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)


# 4 - Slice out the middle item or items from the food_stuff_tp tuple or food_stuuf_lt list
print(food_stuff_tp)
print(len(food_stuff_tp))
first_food_tp = food_stuff_tp[:6]
print(first_food_tp, len(first_food_tp))
second_food_tp =food_stuff_tp[7:]
print(second_food_tp, len(second_food_tp))
print(first_food_tp+second_food_tp, len(first_food_tp+second_food_tp))


# 5 - Slice out the first three items and the last three items from de footd_staff_lt list
print("\nAll the items in the list are ", food_stuff_lt)
print("\nThe first three items are ", food_stuff_lt[0:3])
print("\nThe last three items are ", food_stuff_lt[-3:])


# 6 - Delete the food_staff_tp tuple completely
del food_stuff_tp


# 7 - Check if an item exist in tuple: (Estonia and Iceland)
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
print("The Iceland is in the list?", 'Iceland' in nordic_countries)


# 8 -