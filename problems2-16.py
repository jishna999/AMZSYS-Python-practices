# Problem 16: Write a function extsort to sort a list of files based on extension.

def exsort(li):
    result = sorted(li, key=lambda x: x.split('.')[-1])
    print(result) 
            
exsort(['my.txt','jishna.mkv'])