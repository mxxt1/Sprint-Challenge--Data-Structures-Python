# # Binary search tree from Data Structures assignment
# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     # if value less than node val ---> left
#     # if value greater than node val ---> right
#     def insert(self, value):
#         if value < self.value:
#             if self.left is None:
#                 self.left = BSTNode(value)
#             else:
#                 self.left.insert(value)
#         if value >= self.value:
#             if self.right is None: 
#                 self.right = BSTNode(value)
#             else:
#                 self.right.insert(value)

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         # if search value is node value return true
#         if target is self.value:
#             return True
#         # if the value is less than node value, check to see if node at left and then move to that node
#         elif target < self.value:
#             if self.left is None: 
#                 return False
#             else:
#                 return self.left.contains(target)
#         elif target > self.value:
#             if self.right is None:
#                 return False
#             else:
#                 return self.right.contains(target)

#     # Return the maximum value found in the tree
#     # move along right nodes, if there's a right node, it's value is larger than current node value, so move right. If there is no right node, then current node value is max value
#     def get_max(self):
#         if self.right:
#             return self.right.get_max()
#         else: 
#             return self.value

#     # Call the function `fn` on the value of each node
#     def for_each(self, fn):
#         # call the function on value
#         fn(self.value)

#         if self.left:
#             self.left.for_each(fn)
#         if self.right:
#             self.right.for_each(fn)


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)    
        # compare to the new value we want to insert

        if value < self.value:
            # IF self.left is already taken by a node
                # make that (left) node, call insert 
            # set the left to the new node with the new value
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
            
        if value >= self.value:
            # IF self.right is already taken by a node
                # make that (right) node call insert 
            # set the right child to the new node with new value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value is more than target
        found = False
        if self.value >= target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value is less than target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found
        
    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        # if we cannot go right, return the current value
        if self.right is None:
            return self.value
        max_val = self.right.get_max()



