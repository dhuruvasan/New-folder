def kunfu(n,arr):
    ans=0
    i=0
    while(i<=n):
        if(i==n):
            ans=ans+arr[-1]
        else:
            if(i==n-1):
                if(arr[i]+1==arr[-1] or arr[i]-1==arr[-1]):
                    ans=ans+arr[i]
                    i=i+2
            else:
                if arr[i]+1 == arr[i+1] or arr[i]-1==arr[i+1]:
                    ans=ans+arr[i]
                    i=i+1
                elif arr[i]==arr[i+1]:
                    ans=ans+arr[i]
        i=i+1
    print(ans)




n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
kunfu(n,arr)