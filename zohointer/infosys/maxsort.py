def check(a):
    n=len(a)
    c=[]
    for i in range(n-1):
          c. append(a[i]+a[i+1])
    return c

n=int(input())
a=[]
for i in range(n):
    a.append(int (input()))
a.sort()
a1=a[::2]
print(a1)
a2=a[1::2]
print(a2)
a3=a2[::-1]
b=a1+a3
while(len(b)!=1):
     b=check(b)
print (b[0])