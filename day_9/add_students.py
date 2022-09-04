import random


aleatorio = random.randrange(0,100,1)

# firstname = input("Enter your first name: ")
# lastname = input("Enter your last name: ")
# age = int(input("Enter your age: "))
# country = input("Your country: ")
# city = input("Your city: ")
# street = input("Your street: ")
# zipcode = int(input("Your zipcode: "))






profile = {'profile':{'first_name':'a',
                  'last_name':'a',  
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
                     }
        }
                
    
                            
subjects = ['Mathematics', 'English', 'Spanish', 'Filosofy', 'Physical_Education', 'Theater', 'Programming' ]
for scores in subjects:
     user=int(input("Enter your score of "+ scores + ": "))
     profile[scores]=user

print("The profile length is:",len(profile))
ID = print("Your ID is: ",aleatorio)

print("The profile is:", profile)






print("[<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  DATOS  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]")

'''

ID : Dictionary
Profile : Dictionary
firstname : item String
lastname : item string
age : item integer
address : Dictionary
country : item string
city : item string 
street : item string
zipcode : item string

scores : Dictionary
Maths : item integer
English : item integer
Spanish : item integer
Filosofy : item integer
GyM : item integer
Theatre : item integer
Programming : item integer


# Maths = int(input("Enter your score of {}")).format(subjects)
# English = int(input("Enter your score of Maths"))
# Spanish = int(input("Enter your score of Maths"))
# Filosofy = int(input("Enter your score of Maths"))
# # GyM = int(input("Enter your score of Maths"))
# # Theatre = int(input("Enter your score of Maths"))
# # Programming = int(input("Enter your score of Maths"))




1- Create a new profile
	1-Yes / 2-No
	
1.2 (NO) Modify (options)


  Access for ID  
                   _first name
	_ 1 - profile /_ last name
	|     (name)  \_ age
	|	     |         _ country
	|	     |_address/_ city			
   ID                 \_street    
	|   		       \_zipcode
    |
    |              __ Maths
	|             |
	|             |_ English
	|             |
	|	          |_ Spanish	
	|_ 2 - scores_| 
                  |_ Filosofy
		          |
		          |_ GyM
    	          |
                  |_ Theatre
                  |
                  |_ Programming		


1.1 (YES) Create a new profile whit a new random ID



  NEW ID       _first name
	_ 1 - profile /_ last name
	|     (name)  \_ age
	|	     |         _ country
	|	     |_address/_ city			
   ID                 \_street    
			           \_zipcode
    |
    |                 __ Maths
	|                 |
	|                 |_ English
	|             |
	|	          |_ Spanish	
	|_ 2 - scores_| 
                  |_ Filosofy
		          |
		          |_ GyM
    	          |
                  |_ Theatre
                  |
                  |_ Programming	
'''

