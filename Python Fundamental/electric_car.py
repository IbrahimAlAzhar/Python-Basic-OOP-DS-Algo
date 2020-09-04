from car import Car

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