# Problem 28: Write a function enumerate that takes a list and returns a list of tuples containing (index,item)
# for each item in the list.

def enumerate_new(li):
    new_list=[(li.index(x),x) for x in li]
    return new_list

for index,value in enumerate_new(['a','b',3]):
    print(index,value)
