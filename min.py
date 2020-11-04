def min(a):
    m = a[0]
    for i in a:
        if i<m:
            m = i
    return m

x = [5,6,4,7,9]
y = min(x)
print(y)
