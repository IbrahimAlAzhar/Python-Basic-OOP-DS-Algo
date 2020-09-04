#import python_tutorial
from python_tutorial import make_pizza

make_pizza(16,'mushroom')
make_pizza(18,'mushroom','peppreoni','extra chesse')

class Dog():
    def __init__(self,name,age,):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting ")

    def roll_over(self):
        print(self.name.title() + " roll over")

my_dog = Dog('willie',5)
print("My dog name is " + my_dog.name.title() + ".")
print("MY do is " + str(my_dog.age) + " years old")

your_dog = Dog("lucy",6)
print("your dog name is " + your_dog.name.title() + ".")


class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi','a4','2006')
print(my_new_car.get_descriptive_name())