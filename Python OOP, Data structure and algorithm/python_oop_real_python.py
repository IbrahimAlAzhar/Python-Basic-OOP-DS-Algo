# when you define a new class,Python 3 it implicitly uses object as the parent class
class Dog:
    # class attributes (it is same for all instances),every dog will be a mammal
    species = 'mammal'
    
    def __init__(self,name,age): # use init method to initialize an object's initial attributes by giving them their default value,this method must have at least one argument as well 
        # instance attributes( instance attributes are specific to each object)
        self.name = name  # as the self variable,which refers to the object itself
        self.age = age # self variable which will keep track of individual instances of each class,when you create a new Dog instance __init__ method gets called automatically

    # instance methods are defined inside a class are used to get the contents of an instance,they can also be used to perform operations with the attributes of our objects like the __init__ method,the first argument is always self
    def description(self): # instance method
        return "{} is {} years old".format(self.name,self.age) # .format works as a first print the name then age

    def speak(self,sound): # here takes the 'sound' value as a parameter
        return "{} says {}".format(self.name,sound)


# child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self,speed): # if you wants to add attribute in child class,you have to define with method,you can't use init method,because this one is using on parent class
        return "{} runs {}".format(self.name,speed)


# child class (inherits from Dog class),special breed of Dog
class Bulldog(Dog):
    def run(self,speed):
        return "{} runs {}".format(self.name,speed)


# child classes inherit attributes and behaviors from the parent class
jim = Bulldog("jim",12) # here define the attributes of parent class
print(jim.description())

# child classes have specific attributes and behaviors as well
print(jim.run("slowly"))

# is jim an instance of Dog() ?,yes because jim is instance of Bulldog class which means it also instance of Dog class
print(isinstance(jim, Dog))

# is julie an instance of Dog() ?
julie = Dog("Julie",100) # yes,because Julie directly instance of Dog class
print(isinstance(julie,Dog))

# is johhny walker an instance of Bulldog()
johhnywalker = RussellTerrier("Johhny walker",4)
print(isinstance(johhnywalker,Bulldog)) # johnywaler is instance of RusselTerrier class,which is sub class of Dog class,Bulldog is another sub class of Dog class

# is julie is and instance of jim?
# print(isinstance(julie,jim)) # you can't check this,because jim has to be a class,but here it is just instance of Bulldog class

# instantiate the Dog object
philo = Dog("Philo",5)  # created a new instance of Dog() class and assigned it to the variable philo, pass two arguments which is name and age
mikey = Dog("Mikey",6)  # when you create a new instance of the class python automatically determines what self is (a Dog in this case) and passes it to the __init__ method

# access the instance attributes
print("{} is {} and {} is {} ".format(philo.name, philo.age, mikey.name,mikey.age))

# is Philo a mammal ?
if philo.species == 'mammal':
    print("{0} is a {1}!".format(philo.name,philo.species)) # we can set 0 and 1 in parameter or not,no problem

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))


class Email:
    def __init__(self):
        self.is_sent = False

    def send_mail(self): # here we added a method to send an email,which update the is_sent variable to True
        self.is_sent = True


my_email = Email()
print(my_email.is_sent)
print(my_email.send_mail())


class Dog:
    def __init__(self,breed):
        self.breed = breed


spencer = Dog("German Shepard") # here pass the parameter to Dog class
sara = Dog("Boston Terrier")
print(spencer.breed) # print the attribute of instance
print(sara.breed)


# overriding the functionality of a parent class
# child classes can also override attributes and behaviors from parent class
class Dog:
    species = 'mammal'


class SomeBreed(Dog): # SomeBreed class is sub class of Dog class
    pass


class SomeOtherBreed(Dog):
    species = 'reptile' # override the species from parent class


frank = SomeBreed()
print(frank.species)
beans = SomeOtherBreed()
print(beans.species)


'''
# we do this code in python shell
class Dog: # defining a new Dog() class
    pass
Dog() # created two new dogs,each assigned o different objects 
Dog()
a = Dog() # instantiated two more dogs,assigning each to a variable
b = Dog()
a == b # tested if those variables are equal
ans: False
'''

