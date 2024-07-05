

# # Problem 34: Improve the above program to print the words in the descending order of the number of occurrences.

def desending(words):
    f1={}
    # print(f)
    for w in words:
        f1[w]=f1.get(w,0)+1
    return dict(sorted(f1.items(),key=lambda item:item[1],reverse=True))


print(desending("hi hi hi my my name is jishna how are you".split()))