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
    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("The quantity of gas in the car is: " + str(self.fill_gas) + " litre.")
