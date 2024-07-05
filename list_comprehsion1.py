a = range(10)
print(a)
print([x for x in a])
print([x*x for x in a])
print([x+1 for x in a])
print([x for x in a if x%2==0 and x!=0])

a=[1,2,3,4,5]
b=[6,7,8,9,0]

print([i+j for i,j in (zip(a,b))])

# nested for used in list comprehnsion

print([(x, y) for x in range(5) for y in range(5) if (x+y)%2 == 0])
print([(x,y) for x in range(5) for y in range(5) if (x+y)%2==0 and x!=y])

# pythagorean theorum
print([(x, y, z) for x in range(1, 25) for y in range(x, 25) for z in range(y, 25) if x*x + y*y == z*z])

