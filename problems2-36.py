# Problem 36: Write a program to find anagrams in a given list of words. Two words are called anagrams if one word
# can be formed by rearranging letters of another. For example 'eat', 'ate' and 'tea' are anagrams.

def anagram(li):
    new_list = []
    for i in li:
        for j in range(len(i)):
            new_list.append(j)
    print(new_list)


li = ['ate', 'eat', 'mam', 'jishna']
anagram((li))
