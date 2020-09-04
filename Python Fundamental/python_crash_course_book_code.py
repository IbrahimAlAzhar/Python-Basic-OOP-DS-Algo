
'''
message = "hello python crash courese reader"
print(message)
# print(mesage)
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavascript")
favourite_language = 'python  '
print(favourite_language)
print(favourite_language.rstrip())
language = ' Javascript  '
language = language.strip()
print(language)
message = "one of the python's strengths is its diverse community"
print(message)
age = 23
message = "happy " + str(age) + "rd birthday"
print(message)

bicycales = ['trek','cannondale','redline','specialized']
print(bicycales[0])
print(bicycales[0].title())
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ferrari')
print(motorcycles)
motorcycles.insert(0,'ford')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " +too_expensive.title() + " is to expensive for me.")
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
cars.sort(reverse=True)
print(cars)
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)
players = ['charles','martina','michael','florence','eli']
print("here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("my favorite foods are:")

my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods[:]
my_foods.append('mangoe')
friends_foods.append('jack fruit')
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friends_foods)

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
print(my_foods)
print(friend_foods)

dimensions = (200,50)
print(dimensions[0])
print(dimensions)
# dimensions[0] = 219 # doesn't assign value in tuple
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)

cars = ['audi','bmw','subaru','toyota']
print()
age_0 =22
age_1 = 18
print(age_0>=21 or age_1>=21)
print(age_0>=21 and age_1>=20)
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
banned_users = ['andrew','carolina','david']
user = 'marrie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")

age =12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza")

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','green peppers','extra cheese']
for i in requested_toppings:
    if i in available_toppings:
        print("Adding " + i + ".")
    else:
        print("Sorry we don't have  " +i + ".")

print("\nFinished making your pizza!")

alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print("You just earned " +str(new_points) + " points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_1 = {}
alien_1['color'] = 'black'
alien_1['points'] = 15
print(alien_1)
print("The alien is " +alien_0['color']+ ".")

alien_0 = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}
print("Original x-position: "
+str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# the new position is the old position plus the increment
alien_0['x_position'] =
 alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

alien_2 = {
    'color':'green',
    'points': 5
}
print(alien_2)
del alien_2['points']
print(alien_2)
print("my favourite color is "+
alien_2['color'].title()+".")
user_0 = {
    'username' : 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key,value in user_0.items():
    print("\nKey: "+key)
    print("Value: "+value)

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'azhar':'javascript',
    'phil': 'python'
}
for name,language in favourite_languages
.items(): # if you declare items then shows key,value pair
    print(name.title()+ "'s favorite language is "+ language.title() + ".")

for name in favourite_languages.keys():
    print(name.title())
friends = ['jen','sarah']

for name in favourite_languages.keys(): # using keys for accessing only key terms
    print(name.title())
    if name in friends:
        print(" Hi "+name.title() + ", I see your favourite language is "+favourite_languages[name].title())

for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")

print("The following languages have been mentioned:")
for i in favourite_languages.values():
    print(i.title())

print("The following languages have been mentioned: ")
for i in set(favourite_languages.values
()):
    print(i.title())

# nested dictionaries
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for i in aliens:
    print(i)

aliens = []
for i in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for i in aliens[0:3]:
    if i['color'] == 'green':
        i['color'] = 'yellow'
        i['points'] = 10
        i['speed'] = 'medium'

for i in aliens[:5]:
    print(i)
print("....")

print("Total number of aliens: " + str(len(aliens)))

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print("You ordered a " +pizza['crust'] + "-crust pizza " + "with the following toppings:")
for i in pizza['toppings']:
    print("\t" + i)

favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['ruby','go'],
    'edward': ['c'],
    'azhar': ['python','c++'],
}
for name,languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favourite languages are:")
        for i in languages:
            print("\t" + i.title())
    else:
        print("\n"+ name.title()+ "'s favourite language is:")
        print("\t" + i.title())
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
for username, user_info in users.items():
    print("\nUsername: "+ username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())

message = input("Tell me something, and i will repeat it back to you: ")
print(message)
name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are,we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(name)

age = input("How old are you ?")
age = int(age)
if age>=18:
    print("you are adult")
number = input("Enter a number,and i'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number)+" is even.")
else:
    print("\nThe number "+ str(number)+ " is odd.")
current_number =1
while current_number <=5:
    print(current_number)
    current_number +=1

prompt = "\nTell me something,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

prompt = "\nTell me something,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go "+ city.title() + "!")

current_number = 0
while current_number < 10:
    current_number +=1
    if current_number %2 ==0:
        continue
    print(current_number)

current_number = 0
while current_number < 10:
    current_number +=1
    if current_number ==5:
        break
    print(current_number)

unconfirmed_users = ['alice','brain','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+ current_user.title())
    confirmed_users.append(current_user)

print("The following users have been confirmed:")
for i in confirmed_users:
    print(i)
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?") # take name input and store in name variable
    response = input("Which mountain would you like to climb someday?") # take response input and store it to response variable
    responses[name] = response # store the response value in name index in responses dictionary
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n-- Poll Results--")
for name,response in responses.items():
    print(name + " Would like to climb "+ response + ".")

responses = {}
polling_active = True
while polling_active:
    name = input("\nType your name?")
    response = input("What is your favourite language?")
    responses[name] = response
    repeat = input("Would you like to continue? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n--Poll Results--")
for name,response in responses.items():
    print(name + "'s favourite language is " + response + ".")


def greet_user():
    """Display a simple greeting"""
    print("Hello user")


greet_user()


def hello_user(username):
    print("Hello Mr." + username.title() + " How's your day going.?" )


hello_user('azhar')


def programming_lang(first_n,last_n,language):
    """This function is describe about programming language"""
    username = first_n + last_n
    print("The name of a user is " + username.title() + ".")
    print("Preferred language of " + first_n.title() + "'s is " + language + ".")


programming_lang('azhar','ibrahim','python')
programming_lang('mr.', 'ali', 'c' )
programming_lang(first_n='Mr',last_n='modon mia',language='javascript')
programming_lang(last_n='suna',first_n='mia',language='java')



def describe_animal(pet_name,pet_name_two='cat'):
    print("The pets are" + pet_name + "," + pet_name_two)


describe_animal('cat','monkey')
describe_animal('tiger')

def get_formatted_name(first_name,last_name):
    username = first_name + last_name
    return username
name = get_formatted_name('ibrahim al','azhar')
print(name)
def get_formated_name(first_name,middle_name,last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
name = get_formated_name('ibrahim','al','azhar')
print(name)

def formated_name(first_name,last_name,middle_name=''):
    if middle_name:
        username = first_name + ' ' + middle_name + ' ' + last_name
    else:
        username = first_name + ' ' + last_name
    return username
name = formated_name('ibrahim','azhar')
print(name)
def build_person(first_name,last_name):
    """Return a dictionary of information about a person"""
    person = {'firt':first_name, 'last':last_name}
    return person
musician = build_person('ibrahim','azhar')
print(musician)
def build_person(first_name,last_name):
    person = {'first':first_name, 'last':last_name}
    return person
musician = build_person('ibrahim','azhar')
print(musician)
def build_person(first_name,last_name,age=''):
    personal_info = {'first':first_name,'last':last_name,'age':age}
    return personal_info
person = build_person('Mr','kodom ali',age=34)
print(person)

def get_formated_name(first_name,last_name):
    username = first_name + ' ' + last_name
    return username
while True:
    first_n = input("Enter the first name:")
    last_n = input("Enter the last name:")
    name = get_formated_name(first_n,last_n)
    print(name)
    close = input("If you want to close then press [yes/no}:")
    if close == 'yes':
        break
def build_person(first_name,last_name,age=''):
    personal_info = {'first':first_name,'last':last_name,'age':age}
    return personal_info
person = build_person('Mr','kodom ali',age=34)
print(person)

def get_formated_name(first_name,last_name):
    username = first_name + ' ' + last_name
    return username
while True:
    print("Please tell your name:")
    print("(enter 'q' at any time to quit)")
    first_n = input("Enter the first name:")
    if first_n == 'q':
        break
    last_n = input("Enter the last name:")
    if last_n == 'q':
        break
    name = get_formated_name(first_n,last_n)
    print("\nHello, " + name + ".")

def greet_users(names):
    for name in names:
        print("Hello, " +name.title() + "!")

username = ['ibrahim','al','azhar']
greet_users(username)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print("Current design is : " + current_designs + ".")
    completed_models.append(current_designs)

for i in completed_models:
    print(i)

def print_models(unprinted_designs,complete_model):

    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print("The current design is: " + current_designs + ".")
        complete_model.append(current_designs)

def show_complete_model(complete_model):
    for i in complete_model:
        print(i)
unprint = ['Iphone','samsung','xiamoi']
comlete = []
print_models(unprint,comlete)
show_complete_model(comlete)

def print_models(unprinted_designs, complete_model):
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print("The current design is: " + current_designs + ".")
        complete_model.append(current_designs)
    for i in complete_model:
        print(i)

unprint = ['Iphone', 'samsung', 'xiamoi']
comlete = []
print_models(unprint[:], comlete) # here pass the copy of 'unprint' list to the parameter,here original list can't be empty

def make_pizza(*toppings): # here *means we pass as many argument as we want
    print("\nMaking a pizza with the following toppings:")
    for i in toppings:
        print("- "+i)

make_pizza('pepporoni')
make_pizza('pepporoni','mushroom','salad')

def make_pizza(size,*toppings): # here the argument is positional and arbitrary,we should placee first in positional argument and latter all of are arbitrary arguments
    print("\nMaking a " +str(size) + "-inch pizza with the following toppings:")
    for i in toppings:
        print("- " + i)
make_pizza(12,'mushroom')
make_pizza(34,'pepperoni','mushroom','salad')
def build_profile(first,last,**user_info): # '*' means we can pass arbitrary arguments,'**' means we can pass arbitrary argument as a key value pair
    profile = {} # define a empty dictionary
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstain',location='princeton',field='physics') # passing two arguments and one key value pairs dictionary for '**' charachter
print(user_profile)
def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings.")
    for i in toppings:
        print("-" + i)
make_pizza(12,'mushroom','salad','pepperoni')

class Dog(): # when create a instance of class then call init method
    """A simple attempt to model a dog."""
    def __init__(self,name,age): # init method is using for define the attributes of a class,init method is a special method python runs automatically whenever we create a new instance based on the Dog class.
        """Initialize name and age attriubte,it's like constructor,when we want to make an instance from the dog class,we'll provide values for only the last two parameters"""
        self.name = name  # we'll also be able to access these variables through any instance created from the class,self.name = name takes the value stored in the parameter name and stores it in the variable name
        self.age = age # this init method defines for class itself(here Dog's name and age)
    def sit(self): # this one don't need to additional attributes like name or age,the default parameter of a method in a class is self
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.") # using self.name which pass from instance's attribute calling
    def roll_over(self):
        """Simulate rolling over in response to  a command"""
        print(self.name.title() + " rolled over!")

mydog = Dog('willie',6) # we store that instance in the variable my_dog, here create a instance of the class and pass the parameter to constructor(init method)
print("My dog's name is " + mydog.name.title() + ".") # show the name of a mydog instance
print("MY dog is " + str(mydog.age) + " years old.")
mydog.sit()
mydog.roll_over()
mydog_2 = Dog('Tom',10)
print("Now the dog name is: " + mydog_2.name.title() + ".")
print("The age of dog is: " + str(mydog_2.age) + ".")
mydog_2.sit()
mydog_2.roll_over()
'''
class Car():
    """A simple attempt to represent a car."""
    def __init__(self,make,model,year): # take the value from instance
        self.make = make  # which one the value take from the instance we set it to these variables
        self.model = model
        self.year = year
        self.odometer_reading = 0 # we can set the default value of an attribute
        self.fill_gas = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        full_name = str(self.year) + ' ' + self.make + ' ' + self.model # put year,make,model into one string neatly describing the car
        return full_name
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("The car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        """set the odometer reading to the given value"""
        if self.odometer_reading < mileage:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def inrement_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("The quantity of gas in the car is: " + str(self.fill_gas) + " litre.")

class Battery(): # here define a class separately for Electric car's battery(part of Electric car class written as a separate class)
    """A simple attempt to model a battery for an electric car."""
    def __init__(self,battery_size = 70): # here we override the battery_size value which define on ElectricCar class
        """initialize the battery's attribtes"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.battery_size) +"-kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)


class ElectricCar(Car):
    """Represents aspects of a car,specific to electric vehicles"""
    def __init__(self,make,model,year): # using attributes of super class and you can also add this class attribute,the init method takes the information required to make a car instance
        """initialize attributes of the parent class"""
        # self.battery_size = battery_size
        self.battery_size = 50 # we can use the child class attribute by using dot or using parameter on init function
        super().__init__(make,model,year) # here using the attribute of super class,super function is a special function that helps python make connections between the parent and child class
        # self.battery = Battery(70) # we can pass the parameter's value this process also
        self.battery = Battery()  # here Battery instance stored in the attriubte,we can pass the value here for override battery size,using Battery instance(Battery() means the instance of class Battery), to a 'battery' Attribute,any ElectricCar instance will now havee a Battery instance created automatically

    def describe_battery(self):
        print("\nThe battery size is : " + str(self.battery_size) + "-kwh battery") # the concatenation in print is only useable for string
    def fill_gas_tank(self):
        print("The car has doesn't need a gas tank.")

mycar = Car('audi','a4','2016') # make an instance from the car class and store it in the variable,when we make a new car instance,we'll need to speciy a make,model and year for our instance
desc_name = mycar.get_descriptive_name()
print(desc_name)
mycar.update_odometer(23)
# mycar.odometer_reading = 30 # we use dot notation to access the car's ododmeter_reading attribute and set its value directly
mycar.read_odometer()
mycar_3 = Car('Ferari','a6','2020') # Car() means instance of Car class and store it to mycar_3 variable
d_name = mycar_3.get_descriptive_name()
print(d_name)
mycar_3.update_odometer(-1)
mycar_3.read_odometer()
mycar_3.inrement_odometer(21)
mycar_3.read_odometer()
mycar_3.inrement_odometer(100)
mycar_3.read_odometer()
mycar_3.fill_gas_tank()
'''
my_tesla = ElectricCar('tesla','models',2007)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
my_tesla.update_odometer(23)
my_tesla.read_odometer()
my_tesla.inrement_odometer(12)
my_tesla.read_odometer()

#mytesla = ElectricCar('tesla','models',2009,70)
mytesla = ElectricCar('tesla','models','2005')
print(mytesla.get_descriptive_name())
mytesla.describe_battery()
mytesla.fill_gas_tank()
mytesla.battery.describe_battery() # battery is a attribute of mytesla instance
mytesla.battery.get_range()
'''
from collections import OrderedDict # here import OrderDict class from Collections module(build in)
favourite_languages = OrderedDict() # create a instance of OrderDict class and store it to favourite_languages variable,OrderedDict is one type of dictionary where keep track of the order in which key-value pairs are added(retaining the original order)
favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'javascript'
favourite_languages['azhar'] = 'c++'

for key,value in favourite_languages.items():
    print(key.title() + " 's favourite language is " + value.title() + ".")