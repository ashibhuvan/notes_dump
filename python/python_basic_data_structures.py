# List (internally represented as Array)
a = [1, 2, 3, 4]
print(a[-1])
# Subarray slicing is left INCLUSIVE and right EXCLUSIVE
print(a[1:3]) # 2,3

# loops
nums = [10, 20, 30, 40, 50, 60]
for i,v in enumerate(nums):
    print(i, v)

# Basic LinkedList
class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# Stack... can use list as stack
s = [10, 20, 30, 40]
s.pop() # Will pop the last element, LAST IN FIRST OUT 
s.append() # Will add to the end
s[-1] # will return the last element or TOP OF THE STACK
print(len(s)) # will return length


#Queue
# Python has library collections.deque which is double ended queue, you can push and pop from either side
# in constant time

from collections import deque
q = deque()
q.append(50) # 0(1)
q.popleft() # 0(1)
q[0] # Lets you peek at top of the queue or first element
print(len(q))

# HashTable, called dict in python
d = {}
d['a'] = "abc"
print(d['a'])
del d['a']
print(len(d))

# Counter for counting hashable objects. Pass an iterable object
import collections.Counter

word = "occur"
counter = Counter(word)
print(counter) # ['o': 1, 'c':1....]
len(counter) # number of unique elements 

# Set, python default set is a hashset
s = set()
if a in s: # check if in set
    print(a)
s.add('a')
s.discard('s')
# Useful for knowing the existence of keys

#Tree, you need to define it, simple
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
# Can also do the same for n-children by self.next = []    

# IMPORTANT FOR INT COMPARISON
# INFINITY
positive_infinity = float('inf')
negative_infinity = float('-inf')
# Can also use the math module after python 3.5
import math

pos_infinity = math.inf
neg_infinity = -math.inf








