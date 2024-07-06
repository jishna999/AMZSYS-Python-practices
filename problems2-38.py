# Problem 38: Write a function invert dict to interchange keys and values in a dictionary.
# For simplicity, assume that all values are unique.

def invert_dict(dic):

    dii = {x[1]: x[0] for x in dic.items()}
    print(dii)


invert_dict({'x': 1, 'y': 2, 'z': 3})
