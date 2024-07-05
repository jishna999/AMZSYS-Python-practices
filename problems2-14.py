# Problem 14: Improve the unique function written in previous problems to take an optional key function 
# as argument and use the return value of the key  function to check for uniqueness.

def unique(li, key=lambda x: x):
    s = []
    for i in li:
        u = key(i)
        if u not in s:
            s.append(u)
    return s

print(unique(['Python', 'python', 'html', 'css'], key=lambda s: s.lower()))
