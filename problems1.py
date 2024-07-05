# Running interpreter

# Problem 1: Open a new Python interpreter and use it to find the value of 2 + 3.

# Problem 2: How many multiplications are performed when each of the following lines of code is executed?

num=2
def square(x):
    global num
    num=num+10
    return x*x

print(square(5))
print(square(2*5)) #output:2 multiplications

# Problem 3: What will be the output of the following program?

x1 = 1
def f():
    return x1
print(x1)
print(f())

# Problem 4: What will be the output of the following program?

x2 = 1
def f():
    x2 = 2
    return x2
print(x2)
print(f())
print(x2)

# Problem 5: What will be the output of the following program?

# x3 = 1
# def f():
#         y = x3
#         x3 = 2
#         return x3 + y
# print(x3)
# print(f())
# print(x3)

#output will be error

# Problem 6: What will be the output of the following program?

x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print(x, y)

# Problem 7: Write a function count_digits to find number of digits in the given number.

def count_digits(n):
    print("count of the digits:",len(str(n)))
count_digits(342134)

# Problem 8: Write a function istrcmp to compare two strings, ignoring the case.

def istrcmp(s1,s2):
    print(s1.upper() == s2.upper() or s1.lower() == s2.lower())
istrcmp('python','PYThon')

# Problem 9: What will be output of the following program?

print(2 < 3 and 3 > 1)
print(2 < 3 or 3 > 1)
print(2 < 3 or not 3 > 1)
print(2 < 3 and not 3 > 1)

# Problem 10: What will be output of the following program?

x = 4
y = 5
p = x < y or x < z
print(p)

# Problem 11: What happens when the following code is executed? Will it give any error? Explain the reasons.

x = 2
if x == 2:
    print(x)
else:
    print(y)

# Problem 12: What happens the following code is executed? Will it give any error? Explain the reasons.

x = 2
if x == 2:
    print(x)
# else:
    # x + error int this line because of the inavalid syntax