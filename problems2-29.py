# Problem 29: Write a function array to create an 2-dimensional array.
# The function should take both dimensions as arguments. Value of each element can be initialized to None:

def array_dim(i,j):
    
    new_list=[[5 if x == 0 and y == 0 else None  for x in range(j)] for y in range(i)]
    return new_list
print(array_dim(2,3))