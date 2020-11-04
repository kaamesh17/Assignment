def Lsearch(a,n):
    i=0
    while i<len(a):
        if a[i]==n:
            globals()['p']=i
            return True
        i=i+1
    return False
a=[]
x=int(input("Enter number of items in list :  "))
i=0
for i in range(x):
    num=eval(input('Enter numbers : '))
    a+=[num]
n=int(input('Enter a number that you want to search : '))
if Lsearch(a,n):
    print("Found at : ",p)
else:
    print("Not found")
