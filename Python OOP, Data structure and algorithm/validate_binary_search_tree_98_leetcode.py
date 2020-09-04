# definition for a binary tree node.
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val # initially left,right is None,we can pass the value when we create object
        self.left = left
        self.right = right

# class Solution:
  #  def isValidBST(self, root: TreeNode): -> bool:


class InorderViolatedException(Exception):
    pass


class Solution:
    def __init__(self):
        self.__lastInorderValue = None # here define the class var which is None

    def __inorder(self,root): # define a private method and pass argument as a root's value
        if root is None: # if the root is None means empty then terminate this function
            return
        self.__inorder(root.left) # here pass the left value to root, recursive
        if self.__lastInorderValue is not None and self.__lastInorderValue >= root.val: # if the 'lastInorderValue' is not None and this value is greater then 'root' value,then throw an exception
            raise InorderViolatedException()
        self.__lastInorderValue = root.val # when 'lastInorderValue' is smaller then root value then insert it
        self.__inorder(root.right)

    def isValidBST(self, root: TreeNode) -> bool: # this method is boolean
        if root is None: # if the root is empty then return true
            return True

        # use in order traversal
        try:
            self.__inorder(root)
        except InorderViolatedException:
            return False
        return True


