import random


aleatorio = random.randrange(0,100,1)

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
                            'Phylosophy':0,
                            'Physical_Education':0,
                            'Theater':0,
                            'Programming':0}
                            }}
                
    
                            
profile_keys = ID['profile'].keys()
address_keys = ID['profile']['address'].keys()
score_keys = ID['profile']['scores'].keys()
score_values = ID['profile']['scores'].values()
total_keys =len(profile_keys) + len(address_keys) + len(score_keys)

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


print("Este es el perfil que acabas de crear: ",ID)
