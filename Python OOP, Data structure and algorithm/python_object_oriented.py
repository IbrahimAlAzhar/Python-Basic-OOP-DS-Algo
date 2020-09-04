#manually classk, native approach
class NOde:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

     def findvalue(self,data):
        if data < self.data:
            if self.left is None:
                print('Not Found')
            else:
                self.left.findvalue(data)
        elif data>self.data:
            if self.right is None:
                print('Not Found')
            else:
                self.right.findvalue(data)
        else:
            print('Found')





'''
class Employee:
   pass

emp_1 = Employee()
emp_2 = Employee()

emp_1.first= 'Corey'
emp_1.second = 'Scafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay= 5000

emp_2.first= 'Corey'
emp_2.second = 'Scafer'
emp_2.email = 'Corey.Schafer@company.com'
emp_2.pay = 5000

print(emp_1.email)
print(emp_2.first)
#class using constructor


class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay= pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey','scafer',5000)
emp_2 = Employee('Test','user',6000)
print(emp_1+emp_2)
print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_1.first)
print(emp_2.email)
emp_1.fullname()
print(Employee.fullname(emp_1))
'''

