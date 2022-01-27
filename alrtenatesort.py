def alsort(n,arr):
    arr.sort()
    i=0
    k=n-1
    kk=n
    ans=[]
    while(i<kk):
        ans.append(arr[k])
        k=k-1
        kk=kk-1
        ans.append(arr[i])
        i=i+1 
    for i in range(n):
        print(ans[i],end=" ")

len=int(input())
arrr=[]
for i in range(len):
    temp=int(input())

    arrr.append(temp)

alsort(len,arrr)
