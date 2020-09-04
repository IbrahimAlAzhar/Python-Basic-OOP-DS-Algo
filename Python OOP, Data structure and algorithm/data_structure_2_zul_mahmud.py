from Linked_list_zul_mahmud import DoubleLinkedList


# we can also implement stack by using python build in List,then we don't need to use DoubleLinkedList class,in place of 'push' method we apply 'append' and in place of 'pop' method we apply 'remove'
# here we implement Stack using 'LinkedList' Class, which one we created previous python file
class Stack:
    def __init__(self):
        # self.__list = [] # here we can implement stack by using python build in List
        self.__list = DoubleLinkedList() # here using the 'DoubleLinkedList' which one we created on another python file,and store into a private list

    def push(self,val):
        self.__list.add(val) # add is the function of 'DoubleLinkedList'

    def pop(self):
        val = self.__list.back() # 'back' is the function of 'DoubleLinkedList' which returns tail value means top value
        self.__list.remove_last() # remove the last element(top element)
        return val # return the top value

    def is_empty(self):
        return self.__list.size == 0 # size is the variable of 'DobuleLinkedList' class,if the size is zero then return true,otherwise return false

    def peek(self):
        return self.__list.back() # back function returns the tail means top value

    def __len__(self): # override the len method,return the 'list' size, where 'size' is the attribute of DoubleLinkedList function,
        return self.__list.size
'''


# here we implement stack by using python List
class Stack:
    def __init__(self):
        self.__list = []  # create a private list
        self.size = 0  # create a variable of this class initially which value is 0

    def push(self,val):
        self.__list.append(val)
        self.size += 1

    def pop(self):
        val = self.__list.pop() # it means return the last element or top element and store it to 'val' variable
        self.__list.pop()  # or you can using slicing like 'self.__list[:-1]', '-1' define the last element of list or using 'del self.__list[-1]'
        self.size -= 1
        return val

    def is_empty(self):
        return len(self.__list) == 0  # python len define the length,if the length is '0' then return True

    def __len__(self):  # here override the 'len' method
        return self.size

    def peek(self):
        return self.__list.pop() # return the top element means last element


my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(5)
print(len(my_stack))
print(my_stack.peek())
my_stack.push(6)
print(len(my_stack))  # the 'len' method returns the 'list' size and print out here
print(my_stack.pop())
print(len(my_stack))

'''

