from itertools import count
from re import I


print ("\n***********************  EXERCISES DAY 4  ***********************\n")


print("\n__________________Exercises 1__________________\n")
# 1 - Declare an empty list
list = []

print("\n__________________Exercises 2__________________\n")
# 2 - Declare whit more than  item
list = ['White', 'Black', 'Red', 'Blue', 'Yellow']

print("\n__________________Exercises 3__________________\n")
# 3 - Find the length of your list
print(len(list))

print("\n__________________Exercises 4__________________\n")
# 4 - Get the first item, the middle item and the last item of the list
print(list[0])
print(list[2])
print(list[-1])

print("\n__________________Exercises 5__________________\n")
# 5 - Declara a list called mixed_data_types, put your (name, age, height, marital status, address)
mixed_data_types = ['luis', 40, 80, 'single', 'missing 10' ]

print("\n__________________Exercises 6__________________\n")
# 6 - Declare a list variable named it_companies and assing value Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print("\n__________________Exercises 7__________________\n")
# 7 - Print the list using print
print(it_companies)

print("\n__________________Exercises 8__________________\n")
# 8 - Print the number of companies in the list
print(len(it_companies))


print("\n__________________Exercises 9__________________\n")
# 9 - Print the first, middle and last company
print("The first", it_companies[0])
print("The middle", it_companies[3])
print("The last", it_companies[-1])


print("\n__________________Exercises 10__________________\n")
# 10 - Print the list after modifying one of the companies
it_companies[5] = 'greenworld'
print(it_companies)


print("\n__________________Exercises 11__________________\n")
# 11 - Add an IT company to it_companies
it_companies.append('apple')
print(it_companies)


print("\n__________________Exercises 12__________________\n")
# 12 - Insert an IT company in the middle of the companies list
it_companies.insert(4, 'marvel' ) 
print(it_companies)


print("\n__________________Exercises 13__________________\n")
# 13 - Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = 'FACEBOOK'
print(it_companies)


print("\n__________________Exercises 14__________________\n")
# 14 - Join the it_companies list with a string '#'
string = '#'
it_companies.extend(string)
print(it_companies)


print("\n__________________Exercises 15__________________\n")
# 15 - Check if a certain company exist in the it_companies list
print('marvel' in it_companies)


print("\n__________________Exercises 16__________________\n")
# 16 - Sort the list using sort() method
it_companies.sort()
print(it_companies)


print("\n__________________Exercises 17__________________\n")
# 17 - Reverse the list in the descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)


print("\n__________________Exercises 18__________________\n")
# 18 - Slice out the first 3 companies from the list
print(it_companies[3:])


print("\n__________________Exercises 19__________________\n")
# 19 - slice out the last 3 companies from the list
print(it_companies[:-3])


print("\n__________________Exercises 20__________________\n")
# 20 - Slice out the middle IT company or companies from the list
#print(it_companies[:4]+it_companies[5::])   # concatena dos listas, dejando fuera de ambas IBM
print(len(it_companies))    # 10
it_companies.pop(4)         # Elimina el item de index 4 , IBM
print(it_companies)     


print("\n__________________Exercises 21__________________\n")
# 21 - Remove the first IT company from the list
it_companies.remove('marvel')
print(it_companies)


print("\n__________________Exercises 22__________________\n")
# 22 - Remove the middle It company or companies from the list
print(len(it_companies))
del it_companies[3:5]
print(it_companies)


print("\n__________________Exercises 23__________________\n")
# 23 - Remove the last It company from the list
del it_companies[-1]
print(it_companies)


print("\n__________________Exercises 24__________________\n")
# 24 - Remove all IT companies from the list
it_companies.clear()
print("nada", it_companies)


print("\n__________________Exercises 25__________________\n")
# 25 - Destro the It companies list
del it_companies


print("\n__________________Exercises 26__________________\n")
# 26 - Join the following list
frontend = ['HTML', 'CSS', 'JS', 'React', 'Redux']
backend = ['Node', 'Express', 'MongoDB']


print("\n__________________Exercises 27__________________\n")
# 27 - After joining the list in question 26. Copy the joined list and assign it to a variable full_stack
#       Then insert Python and SQL after redux
full_stack = frontend+backend
print(full_stack.index('Redux'))
print(full_stack)
full_stack.insert(5, 'Python')
print(full_stack)
full_stack.insert(6, 'SQL')
print(full_stack)


print("""
[----------------------<> LEVEL 2 <>-------------------]
""")

# 1 - The following is a list of students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1a - Sort the list and find que min and max age
ages.sort()
print(ages)
print("The min age is ", ages[0], "The max age is", ages[-1] )


# 1b - Add the min age and the max age again to the list
ages.append(19)
ages.append(26)
print(ages)


# 1c - Find the median age (one middle item or two middle items divided by two)
print(len(ages))    # 12  "items in the list"
print("The median age is", (ages[6]/2))


# 1d - Find the average age (sum of all items divided by their number) 
total_ages = ages[0]+ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9]+ages[10]+ages[11]
print(total_ages)
print("The average age is", total_ages/12)


# 1e - Find the range of the ages (max minus min)
print("The range is ",(ages[-1]-ages[0]))


# 1f - Compare the value of (min - average) and (max - average), use abs() method
min_average = ages[0]/2
max_average = ages[11]/2
print(min_average)
print(max_average)
print(min_average==max_average)


# 1g - find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print(len(countries)//2)
print(countries[96])


# 1h Divide the countries list into two equals list if it is even is not one more country for the list half
first_middle_countries = countries[:97]
second_middle_countries = countries[97:]
print(len(first_middle_countries))
print(len(second_middle_countries))


# 1i - ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# Unpack:
    # The first three countries 
    # The rest as "scandic countries"

first_country, second_country, third_country, *scandic_countries = countries
print("\nhe first country is:", first_country)
print("\nThe second country is:", second_country)
print("\nThe third country is:", third_country)
print("\nThe rest countries are:\n", scandic_countries)

