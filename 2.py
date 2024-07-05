# Lists

x = [1,2,3,5,6]
print(x[0:5:2])
print("full list:",x[:])
print("full list excluding last item:",x[0:-1])
print("reversed list",x[::-1])
print(3 in x)
print(x.append(9))

# for statement

for i in [12,13,14,15,15]:
    print(i)

print(zip(['a','b','c','d'],[1,2,3,4]))

names=['jishna','devika','anu']
values=[1,2,3]

for names,values in zip(names,values):
    print(names,values)

# sorting list

a=[12,21,1,2,3,487]
print("sorted list",sorted(a))
b=['jsihan','ammu','kavya']
print("sort strings:",sorted(b))
d = [[12,13],[1,2],[11,12],[20,80]]
d.sort()
print("sorting nested",d)

# tuple

e1=(1,2,3)
e2=5,3,4
print(e1,type(e1),"\n",e2,type(e2))
f1=(1)
f2=(2,)
print(type(f1),type(f2))

# sets
s1=set() #empty set
s2={1,2,3,4,5}
print(s2,type(s2))
s3=set([12,13,12])
print(s3)