print("Hello world!")

# Data types

#integers

print(2+3)
print(2**100)

#floats
print(2.3+4.5)

#strings
print("hello"+"world") #concatination
print("hello"*4) #repetion
print(len("jishna")) #length of the string

txt='''hey how are you?  
      how is your day''' # multiline string
print(txt)

print("hi\nJishna\tV\tT") #escape code

#list
li=[1,2,4,5]
print("length of list:",len(li)) #length of the list
print(li[3]) 

#tuple
tu=(1,2,8)
n1, n2, n3 = tu #possible to assign multiple values at once
print(n1,"\t",n2,"\t",n3)

#dictionary
dict={'id':102,
      'name':'Jishna',
      'Qualification':'MCA'}
print(dict,"\n",dict['id'])

#set
s={1,2,3,5,2}
print(s)

#boolean
# True and False

# None-represent nothing
x=None
print(x)
