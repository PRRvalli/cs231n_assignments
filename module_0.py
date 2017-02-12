# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def quicksort(arr):
    if(len(arr)<=1):
        return arr
    pivot=arr[len(arr)/2]
    left=[x for x in arr if x < pivot]
    right=[x for x in arr if x > pivot]
    middle=[x for x in arr if x == pivot]
    print left+middle+right
    return quicksort(left)+middle+quicksort(right)
    

print quicksort([3,6,8,10,1,2,1])
#[1, 1, 2, 3, 6, 8, 10]

s = "hello"
print s.capitalize()  # Capitalize a string; prints "Hello"
print s.upper()       # Convert a string to uppercase; prints "HELLO"
print s.rjust(7)      # Right-justify a string, padding with spaces; prints "  hello"
print s.center(7)     # Center a string, padding with spaces; prints " hello "
print s.replace('l', '(ell)')  # Replace all instances of one substring with another;
                               # prints "he(ell)(ell)o"
print '  world '.strip()  # Strip leading and trailing whitespace; prints "world"

# containers 
# 1.List
xs = [3, 1, 2]   # Create a list
print xs, xs[2]  # Prints "[3, 1, 2] 2"
print xs[-1]     # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'    # Lists can contain elements of different types
print xs         # Prints "[3, 1, 'foo']"
xs.append('bar') # Add a new element to the end of the list
print xs         # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()     # Remove and return the last element of the list
print x, xs      # Prints "bar [3, 1, 'foo']"

# very important for labelling 
'''If you want access to the index of each element within the body of a loop
use the built-in enumerate function:'''
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)
    
nums = [0, 1, 2, 3, 4]
c=0
squares = []
for x in nums:
    squares.append(x ** 2)
    # nums.pop()
    # square[c]=x ** 2 ---> gives an error
    c=c+1    
print squares   # Prints [0, 1, 4, 9, 16]

# variation code reduction 
nums = [0, 1, 2, 3, 4]
cube = [x ** 3 for x in nums]
print cube

nums = [0, 1, 2, 3, 4]
even_square = [x ** 2 for x in nums if x%2==0]
print even_square

# Dictionaries
d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print d['cat']       # Get an entry from a dictionary; prints "cute"
print 'cat' in d     # Check if a dictionary has a given key; prints "True"
d['fish'] = 'wet'    # Set an entry in a dictionary
print d['fish']      # Prints "wet"
# print d['monkey']  # KeyError: 'monkey' not a key of d
print d.get('monkey', 'N/A')  # Get an element with a default; prints "N/A"
print d.get('fish', 'N/A')    # Get an element with a default; prints "wet"
del d['fish']        # Remove an element from a dictionary
print d.get('fish', 'N/A') # "fish" is no longer a key; prints "N/A"

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.iteritems():
    print 'A %s has %d legs' % (animal, legs)

nums=[0,1,2,3,4,5]
even_squares={x:x**2 for x in nums if x%2==0}

           

           






    
