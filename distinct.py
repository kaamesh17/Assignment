def distinct(s):
    d = ''
    for i in range(len(s)): 
        if (indexOf(s[i],d)==-1):
            d = d+s[i]
    return d

def indexOf(c,s):
    r = -1
    for i in range(len(s)):
        if (c==s[i]):
            return i
    return r

print(distinct("hello"))