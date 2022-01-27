def inset(l1,l2,ar1,ar2):
    arr1=[]
    for i in ar1:
        arr1.append(i)

    for i in ar2:
        ar1.append(i)
    ar1.sort()
    ans=[]
    for j in ar1:
        if j not in ans:
            ans.append(j)
    print(str(ans)[1:-1])
    ans2=[]
    for k in arr1:
        for kj in ar2:
            if k not in ans2:
                ans2.append(k)
            if kj not in ans2:
                ans2.append(kj)
    print(ans2)

len1=int(input())
arr1=[]
arr2=[]
for i in range(len1):
    temp=int(input())
    arr1.append(temp)
len2=int(input())
for i in range(len2):
    temp1=int(input())
    arr1.append(temp1)

inset(len1,len2,arr1,arr2)