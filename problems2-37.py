# Problem 37: Write a function value sort to sort values of a dictionary based on the key.


def sort_key(di):
    return [dict(sorted(di.items(), key=lambda x: x[0])).values()]


print("sorted dictionary:", sort_key({'x': 1, 'y': 2, 'a': 3}))
