a=[1,6,8,2,9,1,4]
for i in range(len(a)):
        min_i=i
        print(i)
        for j in range((i+1),len(a)):
            if a[min_i]>a[j]:
                min_i=j
                #print("the value of i : ",i)
                #print(j)
        v=a[i]
        a[i]=a[min_i]
        a[min_i]=v
        #print("the value of 2nd i : ",i)
        #print("the value of 2nd j : ",j)
        print(a)
print("sorted array is ")
print(a)


   # unwanted swaping      apply condition in between 7 and 8
   #7*7-1
   #n*(n-1)
   #n^2-n