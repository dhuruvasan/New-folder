def addcheck(arr,l,T):
    for i in range(l):
        for j in range(i+1,l):
            if(arr[i]+arr[j]==T):
                print(i,end="")
                print(",",end="")
                print(j)



len=int(input())
arr=[]
for i in range(len):
    temp=int(input())
    arr.append(temp)
T=int(input())
addcheck(arr,len,T)