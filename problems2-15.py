# Problem 15: Reimplement the unique function implemented in the earlier examples using sets.

def unique(li, key=lambda x: x):
    s=set()
    for i in li:
        u = key(i)        
        if u not in s:
            s.add(u)
    return s

print(unique(['Python', 'python', 'html', 'css'], key=lambda s: s.lower()))
