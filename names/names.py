import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1: --> loop through first list O(n)
#     for name_2 in names_2: --> loop through second list O(n)
#         if name_1 == name_2: --> compare the two O(1)
#             duplicates.append(name_1) --> append the duplicate to duplicates O(1)

# NESTED FOR LOOP COMPLEXITY O(n*m)
#O(n) * O(m) * O(1) * O(1)
# Executes in .12168

# MVP
# # create tree
# tree = BSTNode("A")
# # loop and populate the tree with first list
# for first in names_1: # O(n)
#     tree.insert(first)
# # loop through the second list and see if name exists in tree
# for second in names_2: # O(m)
# # if it the name exists, append it to the duplicates list
#     if tree.contains(second): # O(1)
#         duplicates.append(second) # O(1)

# # O(n+m)*O(1)*O(1) = O(n+m)

# STRETCH
# .0043 seconds!!!
for name in set(map(str.rstrip,names_1)).intersection(map(str.rstrip,names_2)):
    duplicates.append(name)

# 1.397 seconds
# for first in names_1:
#     if first in names_2:
#         duplicates.append(first)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.





