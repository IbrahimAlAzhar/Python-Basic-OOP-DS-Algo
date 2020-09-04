from car import Car
from electric_car import ElectricCar,Battery
# import car
# from car import * # here importing all classes from a module

# my_new_car = car.Car('vlokswagen,'beatle',2016)
# print(my_new_car.get_descriptive_name())
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.increment_odometer(70)
my_new_car.read_odometer()

# my_tesla = car.ElectricCar('tesla','roadster',2016)
# print(my_tesla.get_descriptive_name())
my_tesla = ElectricCar('audi','m4',2020)
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

