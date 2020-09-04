from Queue_data_str_zul_m import Queue
from data_structure_2_zul_mahmud import Stack


class TreeNode:
    def __init__(self,val):
        self.left = None # initially left,right is None and val is passing from argument
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None # initially root is None

    def insert(self,val): # insert the value using Queue(FIFO),serially
        if self.root is None: # root is None means there are no root initially
            self.root = TreeNode(val) # create a object of 'TreeNode' class and pass the value and store it to 'root' class variable
            print(self.root.val)
        else:
            nodes = Queue() # create a object of Queue class
            nodes.enqueue(self.root) # always start from root for inserting each node, store the root node in the queue
            print(self.root.val)

            while True: # when return keyword occurs then terminate the function,otherwise it iterate
                checking_node = nodes.deque() # remove from queue and store it to 'checking_node' vaiable,after dequeu each node what we work on then we enqueu the left and right node this node(if have),and going on loop
                print(checking_node.val)
                if checking_node.left is None: # if the left position of current node is empty then we set the value to left position
                    checking_node.left = TreeNode(val)
                    print(checking_node.left.val)
                    return # return terminate this 'insert' function, when we insert on left or right node then we don't need to do something else,so we have to return for safety purpose
                elif checking_node.right is None: # if the right node is empty then store the value on right side by creating a object of 'TreeNode' class and pass the value
                    checking_node.right = TreeNode(val)
                    print(checking_node.right.val)
                    return # return terminate this 'insert' function, when we insert on left or right node then we don't need to do something else,so we have to return for safety purpose
                else: # if there are no empty position on left side or right side then enqueue in a queue then we can work on FIFO order,and check left and right node untill we find a empty position
                    nodes.enqueue(checking_node.left) # after using these nodes on a tree we add into the queue
                    nodes.enqueue(checking_node.right)
                    print(checking_node.left.val)
                    print(checking_node.right.val)

    def contains(self, val):
        nodes = Stack()
        nodes.push(self.root)  # initially push the root node

        while not nodes.is_empty():  # if the stack is empty then terminate the while loop
            node = nodes.pop()  # pop the top element
            print("Checking node:", node.val)
            if node.val == val:  # if we find the value which one we try to find out then return true
                return True
            if node.right is not None:
                nodes.push(node.right)
            if node.left is not None: # using stack and check left is not None,push into Stack,and check over and over
                nodes.push(node.left)


        return False  # if you don't find the number in stack then return False


class BST: # in Binary Search Tree, the left side is smaller then middle value and right side is greater then middle value,but Binary Tree doesn't follow this rules
    def __init__(self):
        self.root = None # initially root node is None

    def __insert_value(self,node,value): # after recursion 'node' is node.right or node.left, take root(always) and insert a node's value
        if node is None: # if node is None then terminate this function
            return  # redundant portion

        if node.val == value: # 'val' is attribute of 'TreeNode' class,if the node value is same as the value which one you store then return(terminate this function),because in BST there are no duplicate number
            return
        elif value < node.val: # if the parameter value is small from node value and the left position of node is None then insert this node,otherwise do recursion
            if node.left is None: # if the left position of this node is empty then make a object of TreeNode and pass the value to this node
                node.left = TreeNode(value)
                print(node.left.val)
                return  # here you insert the value to left side of node,so return and terminate this function
            self.__insert_value(node.left,value) # if the node.left is not none then call this function again,pass node.left which is node right now,and pass the value

        else: # if the value is greater than node.right
            if node.right is None: # if the right position of node is empty then create a object of 'TreeNode' with value and store it
                node.right = TreeNode(value) # after store the value return means terminate this function
                print(node.right.val)
                return
            self.__insert_value(node.right,value) # if the right position of node is not empty then pass the parameter where current node is node.right

    def insert(self,val): # using DFS(Recursive)
        if self.root is None:
            self.root = TreeNode(val) # initially the root node is none,and here create 'TreeNode' object and pass a par
            print(self.root.val)
        else:
            self.__insert_value(self.root,val) # pass this function with root(always) and value

    def __in_order(self,node): # the output is like sorting
        if node is None: # if node is empty then terminate this function
            return # return means teminate the function when there are no node left
        self.__in_order(node.left) # at first recursively take the leftmost value,then print it recursively,then goes to the middel side recursively then right side,if the right side is empty then turn back and go to root node,then again go to left side and if find anything else print it
        print(node.val, end=" ") #  firstly print left value,then middle value then right side value(which is called in order)
        self.__in_order(node.right) # when go to left most side and print it recursively,then go to middle,then go to right side and again find the left child of right side and print it

    def in_order(self):
        self.__in_order(self.root) # pass the root value

    def contains(self,val):
        nodes = Stack()
        nodes.push(self.root) # initially push the root node

        while not nodes.is_empty(): # if the stack is empty then terminate the while loop
            node = nodes.pop() # pop the top element
            print("Checking node:",node.val)
            if node.val == val: # if we find the value which one we try to find out then return true
                return True
            elif val < node.val: # if the val is smaller then node value then we go to the left side
                if node.left is not None:
                    nodes.push(node.left)
            else:  # when 'val' is greater then node value then go to the right side
                if node.right is not None:
                    nodes.push(node.right)
        return False # if you don't find the number in stack then return False


'''
my_tree = BinaryTree()
my_tree.insert('1')
my_tree.insert('2')
my_tree.insert('3')
my_tree.insert('4')
my_tree.insert('5')
my_tree.insert('6')
my_tree.insert('7')
'''

'''
bst = BST()
for i in [8,2,1,10,100,50,40,23,16,7,9,200,150,300]:
    bst.insert(i)
bst.in_order()
print()
print("Containers 150:", bst.contains(150))
print("Containers 0:",bst.contains(0))
'''
bst = BinaryTree()
for i in [8,2,1,10,100,50,40,23,16,7,9,200,150,300]:
    bst.insert(i)

print()
print("Containers 150:", bst.contains(150))
print("Containers 0:",bst.contains(0))

