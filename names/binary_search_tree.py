# Binary search tree from Data Structures assignment
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # if value less than node val ---> left
    # if value greater than node val ---> right
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None: 
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if search value is node value return true
        if target is self.value:
            return True
        # if the value is less than node value, check to see if node at left and then move to that node
        elif target < self.value:
            if self.left is None: 
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    # move along right nodes, if there's a right node, it's value is larger than current node value, so move right. If there is no right node, then current node value is max value
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else: 
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function on value
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
