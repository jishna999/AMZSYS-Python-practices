# Problem 25: Python provides a built-in function map that applies a function to each element of a list.
# Provide an implementation for map using list comprehensions.

def square(x):
    return x*x

def map_new(square,key):
    new_list=[square(x) for x in key]
    return list(new_list)

print(map_new(square,range(5)))

