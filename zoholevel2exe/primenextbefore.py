# A-4: Write a function that takes input as an integer number and prints the
#                                                                closest prime integer to that
# number. The closest prime can be greater or smaller than the passed
#                                                             input integer. If there are equi-
# distant prime-numbers, print both.
# Example:
# Input#1: 32
# Output#1: 31
# Input#2: 30
# Output#2 29 31

from re import T


def fun2(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    else:
        return False

def fun(val):
    va=val+val
    for i in range(val,1,-1):
        n=i-1
        k=fun2(n)
        if(k==True):
            mi=n
            break
    for i in range(val,va,1):
        nn=i
        k=fun2(nn)
        if(k==True):
            ma=nn
            break
    if (abs(mi-val))==(ma-val):
        print(mi,end=" ")
        print(ma)
    else:
        print(mi)

val=int(input())
fun(val)