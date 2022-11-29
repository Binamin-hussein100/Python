# Normal variable Assignment.

counter =  100 # integer assignment
miles = 100.0 # float assignment
name = "John Smith" # string assignment

# Multiple assignment
# Python allows you to assign a single value to severar variables simultaneously
a = b = c = 23

print(a) # 23
print(b) # 23
print(c) # 23
 

# PYTHON STANDARD DATATYPES

# Numbers
23 # integer
15.3 # float
# 535633629843L # long
# 45.j # complex number

# Strings
"Hello" # string
"World" # string

 # Subsets of the strings can be taken using the slice operator
name = "hello world!"
print(name[2:5]) # llo

# Lists
listy = [1,2,3,4,5] # list
[1,"john", 43,["g","k"]] # list containing different datatypes.
# values of a list can be accessed using the slice operator [:]
print(listy[0]) # [1,2,3]

# Tuples ==> READ-ONLY lists
tinyTuple = (123,"john") 

# updating a tuple is not supported
# tinyTuple[0] =  14 # TypeError: 'tuple' object does not support item assignment


