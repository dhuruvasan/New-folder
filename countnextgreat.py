def fun(n,arr):
    k=0
    for i, j in enumerate(arr[:-1]):
        if j<=arr[i+1]:
            k+=1
    print(k+1)

n=int(input())
arr=[]
for i in range(n):
    l=int(input())
    arr.append(l)

fun(n,arr)