a= "hello"
f = {} 
for i in a: 
    if i in f: 
        f[i] += 1
    else: 
        f[i] = 1
print ("Count of all characters in hello is :\n "
                                        +  str(f)) 
