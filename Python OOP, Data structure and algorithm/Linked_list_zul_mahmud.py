# double linked list
class Node: # create a class for node where the next and previous node is empty initially
    def __init__(self,value):
        self.next = None
        self.prev = None
        self.val = value  # pass the parameter value and take to 'val' in class


class DoubleLinkedList:
    def __init__(self):
        self.head = None # initially head and tail is 'None' and size is 0
        self.tail = None
        self.size = 0

    def add(self,val):
        node = Node(val) # create a object of 'Node' class with 'val' parameter and store it to 'node' variable
        if self.tail is None:  # if the tail is none it means there are no node inside the link list
            self.head = node # for the first time store the node which is head and tail,increase the size
            self.tail = node
            self.size += 1
        else:   # if there are already has node in linked list
            self.tail.next = node  # here already has node in linked list,so the new node insert after the previous tail
            # print(self.tail.val)
            node.prev = self.tail  # here set the prev value of node is tail value where insert the current node is after the tail node
            self.tail = node  # finally set the tail is current node
            self.size += 1  # increase the size

    def __remove_node(self,node):  # take the parameter for removing which node
        if node.prev is None:  # it means if the node is 'head'
            self.head = node.next # now remove the current 'head' node it means now head is the next node,here 'next' is the attribute of 'Node' class(here class name 'Node' is same as variable 'node',so we can access it)
        else:
            node.prev.next = node.next # when the node is not head or tail then the 'next' of 'previous' node is next of current node,if we try to remove middle node then here it goes to both else condition

        if node.next is None:  # here the node is tail then remove the tail so current tail is 'prev' of current node
            self.tail = node.prev
        else:
            node.next.prev = node.prev # in middle nodes it takes both of else case,and the next of prev takes next of current node, the prev of next node take the prev of current node
        self.size -= 1

    def remove(self, value):
        node = self.head  # take the head using as a 'node'
        while node is not None: # iterate the loop until not None means until tail,the next item of tail is 'none'
            if node.val == value: # 'val' is attribute of 'Node' class,here check which node you want to remove
                self.__remove_node(node) # call the 'remove_node' method(private method) for remove the node, remove all the element which one you passing from parameter
                # break # if we use break statement here then remove only one element not all same elements
            node = node.next  # inside the while loop 'node' is the next node for iterating purpose

    def remove_first(self):
        if self.head is not None:
            self.__remove_node(self.head)

    def remove_last(self): # when this function call,it only remove the last element
        if self.tail is not None: # the tail element is not none then it can remove by using 'remove_node' method
            self.__remove_node(self.tail)

    def front(self):
        return self.head.val  # return the value of head

    def back(self):
        return self.tail.val  # return the value of tail

    def __str__(self): # we override str method,so if we print the object then it show the str method's what are return
        vals = []
        node = self.head  # node is the 'head' of the linked list
        while node is not None:
            vals.append(node.val) # here append the the 'val' of 'Node' class
            node = node.next  # now the node is next item
        return f"[{', '.join(str(val) for val in vals)}]" # each item in 'vals' list,convert to str and join with comma separator


'''
my_list = DoubleLinkedList()  # create a object of the class and store it to 'my_list' variable
my_list.add(1)  # add the node in the linked list
my_list.add(5)
my_list.add(2)
my_list.add(7)
my_list.add(1)  # add the node in the linked list
my_list.add(5)
my_list.add(2)
my_list.add(7)
print(my_list) # here we print the object(consider as a variable),so we have to override the 'str' class otherwise it is printing garbage

my_list.remove(1)
print(my_list)
my_list.remove(5) # remove all the 5
print(my_list)
my_list.remove_first()
print(my_list)
print(my_list.size) # size is the attribute of 'DoubleLinkedList' class,we access it by using object
my_list.remove_last()
print(my_list)
'''