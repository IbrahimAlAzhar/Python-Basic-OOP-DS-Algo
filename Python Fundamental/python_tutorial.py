
message = "hello everyone"
print(message)
name = "ada lovelace"
print(name)
print(name.lower())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())
print("\tPython")
message = "This is my age"
age = 23
print(message + " " + str(age))

bicycles = ['trek','phoneix','abcd']
print(bicycles[1])
bicycles[0] = 'motorala'
print(bicycles[0])
bicycles.append('ferrari')
print(bicycles)
bicycles.insert(1,'food')
print(bicycles)
too_expensive = 'ferrari'
bicycles.remove(too_expensive)
print(bicycles)
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
for car in cars:
    print(car)
even_numbers = list(range(2,20))
print(even_numbers)
squares = []
for value in range(2,20):
    square = value**2
    squares.append(square)
print(squares)

squres = [value**2 for value in range(2,10)] # list comprehension
print(squres)

my_foods = ['pizza','jackfruit','mangoe','banana']
friends_foods = my_foods[:]
my_foods.append('litchi')
print(my_foods)
print(friends_foods)

dimension = (200,120)
print(dimension[0])
# dimension[0] = 160
for dim in dimension:
    print(dim)

cars = ['audi','bmw','subaru','toyota']
print(cars)
age_0 = 22
age_1 = 18
print(age_0>=21 or age_1>=21)
print(age_0>=21 and age_1<=21)
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is &5")
else:
    print("Your adimssion cost is $10")

requested_toppings = ['mushrooms','chilies','poppings']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'chilies' in requested_toppings:
    print("Adding chilies")

# Dictionary
alien_0 = {'color':'green', 'points':5}
print(alien_0['points'])
new_points = alien_0['points']
print("you just earned " + str(new_points) + " points.")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0['x_position'])

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-positionn: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
}
print("Sarah's favourite lanaguage is " + favourite_languages['sarah'].title() + ".")

for a,b in favourite_languages.items():
    print("\nKey " + a)
    print("\nValue " + b)

friends = ['phil','sarah']
for name in favourite_languages.keys():
    print(" Hi " + name.title() + " i see your favourite language is " + favourite_languages[name].title() + "!")

# nesting dictionary
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'red','points':10}
alien_2 = {'color':'yellow','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens = []
for alien in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print(".....")

pizza = {
    'crust': 'thick',
    'toppings': ['mushromms','extra cheese'],
}
print("you ordered a " + pizza['crust'] + " -crust pizza with following toppings")
for topping in pizza['toppings']:
    print("\t" + topping)

users = {
    'aeinstein' : {
        'first': 'albert',
        'last' : "einstein",
        'location': 'princeton',
    },

    'mcurie': {
        'first':'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username,user_info in users.items():
    print("\nUsername: +" + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation "+ location.title())

# how input works on python
message = input("Please enter your name: ")
print(message)
age = input("How old are you ? ")
print(age)
if int(age)>18:
    print("you are adult")

print(4%3)
number = input("Enter a number,and i'll tell you it is odd or even")
number = int(number)
if number %2 == 0:
    print("\nThis number is even")
else:
    print("\nThis number is odd")


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1

message = "."
prompt = "\nTell me something and i will repeat it back to you"
while message != 'quit':
    message = input(prompt)
    print(message)

active = True
while active: # using flag
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("i'd love to go to "+ city.title() + "!")

current_number = 0
while current_number <10:
    current_number +=1
    if current_number %2 == 0:
        continue
    print(current_number)

unconfirmed_users = ['alice','brain','abcd']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user " + current_user.title())
    confirmed_users.append(current_user)

    print("\nFollowing users have been confirmed")

for i in confirmed_users:
    print(i.title())

# function



def get_formatted_name(first_name,last_name,middle_name=''):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name


musician = get_formatted_name('ibrahim','azhar','al')
print(musician)

def build_person(first_name,last_name):
    person = { 'first':first_name,'last':last_name}
    return person

musician = build_person('ibrahim','azhar')
print(musician)

while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello " + formatted_name )


def greet_user(names):
    for name in names:
        msg = "hello " + name.title() + "!"
        print(msg)


usernames = ['mr','hannah','andrew','ibrahim']
greet_user(usernames)

def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + " -inch pizza with the following toppings")
    for i in toppings:
        print(i)


