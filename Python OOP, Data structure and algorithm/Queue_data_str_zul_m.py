from Linked_list_zul_mahmud import DoubleLinkedList
from collections import deque  # it is the build in Queue where you can insert and remove both front side and back side also

# here create a queue by using DoubleLinkedList which one we build on previous python file 
class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enqueue(self,val):
        self.__list.add(val)

    def deque(self):
        val = self.__list.front()  # front is method of DoubleLinkedList class,which returns the head value
        self.__list.remove_first()
        return val

    def front(self):
        return self.__list.front()

    def is_empty(self):
        return self.__list.size == 0 # if the size is zero then return True

    def __len__(self):
        return self.__list.size  # here override the 'len' method and return the list size
'''

# here create a queue by using Python List
class Queue:
    def __init__(self):
        self.__list = []
        self.size = 0

    def enqueue(self,val):
        self.__list.append(val)
        self.size += 1

    def deque(self):
        val = self.__list.pop(0) # 0th index value is first value we insert,when we use this code in BST this pop occurs error
        self.__list.pop(0)  # remove the first index value(0th index)
        self.size -= 1
        return val

    def is_empty(self):
        return len(self.__list) == 0 # if the length is 0,then return True

    def front(self):
        return self.__list.pop(0) # 'front' method returns the 0th index value from queue

    def __len__(self):
        return self.size # return the size of Queue,here override the 'len' method so that we can easily find the len

'''
'''
my_queue = Queue() # create a object of 'Queue' class and store it to a variable
my_queue.enqueue(1)
my_queue.enqueue(3)
my_queue.enqueue(7)
my_queue.enqueue(11)
print(my_queue.front())
print(len(my_queue))
print(my_queue.deque())
print(my_queue.front())
'''
