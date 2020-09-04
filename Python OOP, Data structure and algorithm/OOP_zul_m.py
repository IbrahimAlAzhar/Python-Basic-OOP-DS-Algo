class Person:
    def __init__(self,person_name: str,year_of_birth: int,ht_inches: int = None): # here is a constructor which set the value of class attributes,here define the type of parameter like string,int etc,'None' means if you don't pass the parameter's value it's no problem by default it's initial value is 'None'
        self.__name = person_name # double underscore means that this variable is private,you can't change its value directly,you can use method to change this value,private,public,default which is access modifier in c++ and here it is called encapsulation
        self.__date_of_birth = year_of_birth
        self.__height = ht_inches  # ht is parameter which value pass from instance and set it to class attribute
        self.abc = None

    def get_year_of_birth(self):  # if we want to access the private variable then we have to use a function
        return self.__date_of_birth

    def get_name(self):  # getter method
        return self.__name  # in double underscore variable which is private,we can just use getter method for retrieving its value but we shouldn't use setter method for these attributes

    def set_name(self,new_name): # setter method
        if self._has_any_number(new_name): # if the person has any number then print this command and return,otherwise set the 'name'
            print("Sorry person name can't have number")
            return
        self.__name = new_name

    def _has_any_number(self,string):
        return "0" in string  # return True if the String has 0,otherwise False

    def get_summary(self):
        return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height: {self.__height if self.__height is not None else 'Invalid'}"  # f string prints all of these things in a single line,if the height is not None then print otherwise print 'Invalid'


a_person = Person("ibrahim",1997,5)
# b_person = Person("azhar")
print(a_person.get_summary())
# print(b_person.get_name())
a_person.set_name("0ibrahim al azhar")
print(a_person.get_name())
# a_person.__name = "azhar al ibrahim" # here 'name' attribute is private(encapsulation),so we shouldn't access this way
# print(a_person.__name) # you can't access the private variable which is define using double underscore

person_list = [Person("ibrahim",1997,68), # here creating a list and create Person class object and store it to the list
               Person("azhar",2003,33),
               Person("Mr Ali",1999),
               Person("Mr modon",1990,45)]

for person in person_list:
    if person.get_year_of_birth() >= 1991:
        print(person.get_summary())


class Student(Person):
    def __init__(self, person_name: str, year_of_birth: int, email_id: str, student_id: str): # here the define the attributes of this class and super class
        super().__init__(person_name,year_of_birth) # here define only the attributes of super class(for inheritance)
        self.id = student_id  # this class 'id' is 'student_id' which come from parameter
        self.email = email_id # this class 'email' is 'email_id' which is come from parameter

    def get_summary(self):  # override from super class the 'get_summary' method
        return f"Name: {self.get_name()} Email: {self.email} Birth: {self.get_year_of_birth()} "

    def __str__(self):
        return self.get_summary() # we can return 'get_summary' method instead of return all of those things
        # return f"Name: {self.get_name()} Email: {self.email} Birth: {self.get_year_of_birth()} "

    def __repr__(self):  # this method is using for debugging easily
        # return self.get_summary() # we can return 'get_summary' method instead of return all of those things
        return f"Name: {self.get_name()} Email: {self.email} Birth: {self.get_year_of_birth()}"


student = Student("ibrahim al", 1998, "ibrahimalazhar264@gmail.com","2015331545")
# print(student.get_summary())
print(student)  # in this class we override the 'str' method,so if we print the object(variable) then print all of this,we don't need to call 'get_summary' method
student.set_name("Robert")
# print(student.get_summary()) # if we don't override the __str__ method then we have to print the get summary method
print(student)  # we override 'str' method in class so we can just print object and print out the str method


class Teacher(Person):
    def __init__(self,person_name: str, year_of_birth: int, department:str): # create sub class constructor where super class field is 'person_name' and 'year_of_birth' and sub class field is 'department'
        super().__init__(person_name,year_of_birth)  # here define only super class field which is 'person_name' and 'year_of_birth'
        self.dept = department # set the value of 'dept' by using attribute

    def get_summary(self): # override the 'get_summary' method from super class
        return f"{self.get_name()} is a teacher"


new_person_list = [ # here create a list and the item of list is creating object of each class(super class and sub class
    Person("Ibrahim",2003),
    Student("Azhar",1997,"ibrahimalazhar264@gmail.com","2015331545"),
    Teacher("Robert",1980,"tid")
]

for p in new_person_list:
    print(p.get_summary()) # here print 'get_summary' method of each class


# struct class (a plain class for store the information only)
class PlainClass: # this struct class has no attribute,init function
    pass


abc = PlainClass() # create a object of struct class and store it to abc variable
abc.age = 30  # define the attribute of struct class and store the variable
abc.name = "playboy"
print(abc.name)
print(abc.age)


