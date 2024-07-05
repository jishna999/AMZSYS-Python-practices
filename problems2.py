# Problem 1: What will be the output of the following program?

x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)
x[2] = 2
print(x)

# Problem 2: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.

print(sum([23,56,78]))

# Problem 3: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.

# print(sum(['jishna','vt'])) error will be produce because sum() can only performs with numbers

def sums(s1,s2):
    print("concate",s1+s2)
sums('jishna','vt')

# Problem 4: Implement a function product, to compute product of a list of numbers.

def product(li):
    p=1
    for x in li:
        p=p*x
    return p
print(product([1,2,3,5]))

# Problem 5: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?

def fact(n):
    fa=1
    for i in range(1,n+1):
        fa=fa*i
    print("factorial=",fa)
fact(5)

# Problem 6: Write a function reverse to reverse a list. Can you do this without using list slicing?

def reverse(li):
    print(sorted(li,reverse=True))

reverse([1,2,3,4,5])


# Problem 7: Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation
# for these functions. What happens when you call your min and max functions with a list of strings?

def mini(lst):
    
    minimum = lst[0]
    for item in lst[1:]:
        if item < minimum:
            minimum = item
    return minimum

def maxi(lst):
    maximum = lst[0]
    for item in lst[1:]:
        if item > maximum:
            maximum = item
    return maximum
print(mini([12,3,2,1]))
print(maxi([12,3,2,1]))

# Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
#  Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?

def cumulative_sum(li):
    s,l2=0,[]
    for i in li:
        s=s+i
        l2.append(s)
    return l2
print("cumulative sum=",cumulative_sum([1,2,3,4]))

# Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.

def cumulative_product(li3):
    p,l3=1,[]
    for i in li3:
        p=p*i
        l3.append(p)
    return l3
print("cumulative product=",cumulative_product([1,2,3,4]))

# Problem 10: Write a function unique to find all the unique elements of a list.
# Problem 11: Write a function dups to find all duplicates in the list.


def unique_dup(un):
    u,du=[],[]
    print("original list:",un)
    for i in un:
        if i not in u:
            u.append(i)
        
        else: 
            du.append(i)
    print("unique",u,"\n dupe:",du)
unique_dup([1,2,3,2,1,3,4])

# Problem 13: Write a function lensort to sort a list of strings based on length.

def lensort(lens):
    print("original list",lens)
    print("length sorted:",sorted(lens,key=len))
lensort(['php','c','java','c++'])

