# in object oriented python program,you can restrict access to methods and variables,this can prevent the data from being modified by accident and is known as encapsulation
# Encapsulation,restricted access to methods or variables(private/public/default class/method is encapsulation)


class Car:
    def __init__(self):  # this private function be called on the object directly,only from within the class
        self.__updateSoftware()

    def drive(self):
        print("driving")

    def __updateSoftware(self):  # this is a private method,we can't access this method,when create a instance this method automatically called, here create a private method using underscore,when a car object is created,it will call the private methods __updateSoftware()
        print('updating software')  # we create a private method using underscore


redcar = Car()  # here we create a class and now the private method automatically called
redcar.drive()  # encapsulation prevents from accessing accidentally,but not intentionally
# the private attributes and methods are not really hidden,they're renamed adding '_Car' in the beginning of their name
# the method can actually be called using redcar._Car_updateSoftware()
# a private variable can only be changed within a class method and not outside of the class


class Car:
    __maxspeed  = 0  # it is a private variable,you can change this value only inside the class,not outside the class
    __name = ""  # private string variable

    def __init__(self):
        self.__maxspeed = 200 # we set the value of private variable inside the class,we can't change it outside the class,even we can't pass the value from instance
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed '+ str(self.__maxspeed))

redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # here we try to update the private variable value,but we can't change the  value of private variable
redcar.drive()

# if you want to change the value of a private variable,a setter method is used,this is simply a method that sets the value of a private variable


class Car:
    __maxspeed = 0  # define the private variable
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self,speed):  # we create method for change the value of private variable,otherwise we can't change the value of private variable,using setter method
        self.__maxspeed = speed  # take the argument and set it to the private variable '__maxspeed'


redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()
# other programming language has protected class methods,but python has only private and public methods/variables
# encapsulation gives you more control over the degree of coupling in your code,it allows a class to change its implementation without affecting other parts of the code
