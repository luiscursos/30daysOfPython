import random


print ("\n***********************  EXERCISES DAY 9  ***********************\n")


print("\n[_______________________________EXERCISES LEVEL 1_______________________________]\n")

# 1 → Get user input using input("Enter you age"). 
    # If user is 18 or older, give feedback: You are old enough to drive.
    # If below 18 give feedback to wait for the missing amount of years. Output:


user = int(input("Enter you age: "))

if user >= 18:
    print("You are old enough to drive.")
else:
    print("Wai wait wait until to 18 years old")


# 2 → Compae the values of «my_age» and «your_age» usinf if...else. Who is older(me or you)?
#     use input("Ebter you age: ") to get the age as input. You can use a nested condition to print 'year'
#     for 1 year difference in age, 'years' for bigger differences, and a custom text if «my_age = your_age»

age = int(input("Enter your age : "))
ages_p = int(input("Enter your other age : "))

if age == ages_p:
    print('The same ages')
elif age < ages_p:
    difference_age = ages_p - age
    print("Paco tiene ",difference_age, "màs")
elif age > ages_p:
    difference_age = age - ages_p
    print("Yo tengo ",difference_age,"màs")
else:
    print("Esto es mu raro")




print("\n[_______________________________EXERCISES LEVEL 2_______________________________]\n")

# 1 → Write the code which gives grade to students according to theirs scores

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

ID = {'profile':{'first name':'a',
                  'last name':'a',  
                  'age':0,  
                   'address':{'country':'a', 
                                'city':'a',
                                 'street':'a',
                                    'zipcode':0},
                    'scores':{'Mathematics':0,
                            'English':0,
                            'Spanish':0,
                            'Filosofy':0,
                            'Physical_Education':0,
                            'Theater':0,
                            'Programming':0}
                            }}
                
    
                            
#subjects = ['Mathematics', 'English', 'Spanish', 'Filosofy', 'Physical_Education', 'Theater', 'Programming' ]
profile_keys = ID['profile'].keys()
# print("prueba profile: ", prueba1)
# prueba2 = ID['profile'].values()
# print("prueba data profile: ", prueba2)

address_keys = ID['profile']['address'].keys()
# print("prueba address: ", prueba3)
# prueba4 = ID['profile']['address'].values()
# print("prueba data address: ", prueba4)

score_keys = ID['profile']['scores'].keys()
print("prueba score keys: ", score_keys)
score_values = ID['profile']['scores'].values()
print("prueba score values: ", score_values)
total_keys =len(profile_keys) + len(address_keys) + len(score_keys)
print(total_keys)


count = 0   
for data_profile in ID['profile'].keys():
    if count < 3:
        user = input("Enter your " + data_profile + " : ")
        ID['profile'][data_profile] = user
        count += 1

    elif count == 3:
        for data_address in ID['profile']['address'].keys():
            user = input("Enter your " + data_address + " : ")
            ID['profile']['address'][data_address] = user
            count += 1

    elif (count > 3 and count < total_keys-1):
        for data_scores in ID['profile']['scores'].keys():
            user = int(input("Enter your score in " + data_scores + (" : ")))
            ID['profile']['scores'][data_scores] = user
            count += 1

    else:
        print("Ron da error")


for subjects, score in ID['profile']['scores'].items():
    if score > 90 and score < 100:
        print("In {} obtuvo {} is A".format(subjects, score))
    if score > 70 and score < 89:
        print("In {} obtuvo {} is B".format(subjects, score))
    if score > 60 and score < 69:
        print("In {} obtuvo {} is C".format(subjects, score))
    if score > 50 and score < 59:
        print("In {} obtuvo {} is D".format(subjects, score))
    if score > 0 and score < 49:
        print("In {} obtuvo {} is F".format(subjects, score))


print(ID)





