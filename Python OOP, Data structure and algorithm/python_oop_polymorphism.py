from math import pi

# polymorhic len() function,it returns specific information about specific data types
print(len("Programiz"))
print(len(["python", "java", "c"]))


# python polymorphism in oop,we can use the concept of polymorphism while creating class methods as python allows different classes to have methods with the same name
# python polymorphism means you can use the same method name in different class and you can easily access it
class Cat:
    def __init__(self,name,age):  # this method works like a constructor
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat.My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty",2.5) # make a instance with parameter and store it to a variable
dog1 = Dog("Fluffy",4) # make a instance with parameter and store it to a variable

# here we create same method name info(),make_sound(),they share similar structure

for animal in(cat1,dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

# we don't created superclass there,we can pack these two different objects into a tuple and iterate through it using a common animal variable,it is possible due to polymorphism
# the child class in python also inherit methods and attributes from the parent class,we can redefine certain methods and attributes specifically to fit the child class which is known as method overriding
# polymorphism allows us to access these overriden methods and attributes that have the same name as the parent class


class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two dimensional shape."

    def __str__(self):  # string representation of this class,this method which have not been overridden in the child class,used from the parent class using 'init' method
        return self.name


class Square(Shape):
    def __init__(self,length):  # override the init method of parent class in sub class,add extra parameter 'length'
        super().__init__("Square")  # this one applying 'name' attribute of child class,name is "Square",
        self.length = length

    def area(self):
        return self.length**2  # area is square of length

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self,radius): # override the init method of super class and add extra parameter radius
        super().__init__("Circle") # this one applying the name attribute of child class,name is 'Circle'
        self.radius = radius  # apply the 'radius' attribute value,when create a instance of this model,then pass it

    def area(self):
        return pi*self.radius**2 # area of a circle is pi*(r^2)


a = Square(4)  # create a instance of Square class,and pass the parameter which one define the length
b = Circle(7)  # create a instance of Circle class and pass the parameter which one define the radius
print(b)  # here print the name of "Circle" class which is "Circle"
print(b.fact()) # there are no method name 'fact' in Circle class,but in super class there are a 'fact' method & call it
print(a.fact())  # here apply the method overriding,show the 'fact' method of Square class,don't show 'fact' method of 'Shape' class
print(b.area()) # here print the are of 'Circle' class which overriding of parent 'Shape' class
print(a.area())
