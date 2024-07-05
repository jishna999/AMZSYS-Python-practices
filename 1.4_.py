# variables
x=5
print(x)

#functions
#built-in function
print("hi")
len("123")

#write a program to count the number of digits in number

n1=12345
print("count:",len(str(n1)))

n2=2**100
print("count:",len(str(n2)))

#custom function

def square(x):
    return x*x
print(square(5))
print(square(5)+square(8))
print(square(square(10)))

#using a function inside function body

def sum_of_squares(x,y):
    print(square(x)+square(y))
sum_of_squares(10,11)

#global keyword

num = 0
def square(x1):
    global num #if want to modify the value global scope variable inside the function ,should mention it as global
    num = num + 1
    return x1 * x1
print(square(78))