# Problem 24: Provide an implementation for zip function using list comprehensions.

def zip_new(li1,li2):
    new_list=[(x,y) for x in li1 for y in li2 if li1.index(x) == li2.index(y) ]
    return new_list
print(zip_new([1,2,3],['a','b','c']))