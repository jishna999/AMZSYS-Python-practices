# Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true.
# Provide an implementation for filter using list comprehensions.

def even(x):
       if x%2==0:
             return x

def fil_new(even,key):
    new_list=[even(x) for x in key if even(x) != None]
    return list(new_list)
print(fil_new(even,range(10)))