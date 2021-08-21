# (2) Algorithm Design [3 pts.]

# Suppose you have two lists of numbers (A and B), and some of the numbers may be common
# to both lists. We want to find all these common elements. For simplicity, both lists are of the
# same size (they both have n elements).
# For example:
# A = [6,1,3,2,7,2,2]
# B = [1,4,2,7,5,3,6]
# The elements in common are: [1,2,3,6,7]
# This problem is pretty trivial to solve with a set intersection, which is why you are not allowed to
# use such a tactic. We want you to work with the lists directly by designing an algorithm for doing
# a ‘list intersection’ from scratch, without using any fancy Python tricks.

# A. The default brute force approach is: pick one element from A and scan B for it. What is
# the runtime complexity of brute force in big­O notation?
# B. Can you design an improved algorithm which runs in O(n log n) or better? Only
# pseudocode is required.


def intersection_list(list1, list2):  
   return set(list1) & set(list2)

list1 = [6,1,3,2,7,2,2]
list2= [1,4,2,7,5,3,6]

  
print(intersection_list(list1, list2)) 