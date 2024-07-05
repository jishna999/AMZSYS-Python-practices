# Problem 27: Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. 
# Please note that (a, b, c) and (b, a, c) represent same triplet.

def tripplet(n):
    new_list=[(x,y,z) for x in range(1,n) for y in range(1,n) for z in range((x+y),n) if z==x+y]
    print(new_list)
tripplet(5)