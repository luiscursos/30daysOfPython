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