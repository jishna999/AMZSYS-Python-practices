a={'id':12,
   'name':'jishna',
   'qualification':'MCA'}

print(a['id'])

a['id']=123 #changing value by using key
print(a)

a[(1,2)]="hi" # adding new key value pair
print(a)

del a['id'] # deleting key value pair using del
print(a)

print(a.keys()) # accessing keys from the dictionary

print(a.values()) # accessing values from the dictionary

print(a.items()) # accessing key value pair from the dictionary

for key in a:  
    print(key)

for key,values in a.items(): 
    print(key,values)

print('name' in a) # checking keys in dictionary or not
# b=a.has_key()
# print(b)



print('hello %(name)s' % {'name': 'python'})

#word freqquency

def word_frequency(words):
   
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency
print(word_frequency("hi my name is jishna how are you"))

# Getting words from a file is very trivial.

def read_words(filename):
    return open(filename).read().split()
print(read_words('a.csv'))

# We can combine these two functions to find frequency of all words in a file.

def main(filename):
    frequency = word_frequency(read_words(filename))
    for word, count in frequency.items():
        print(word, count)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
