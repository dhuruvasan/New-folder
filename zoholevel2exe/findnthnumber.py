import re


def rotate(f,listt):
    listt=listt[f-1:]+listt[:f-1]
    return listt

def fun(l,f):
    listt=list(range(1,l+1))
    for i in range(0,len(listt)):
        if len(listt)+1>f:
            print(listt[f-1],end="")
            listt.remove(listt[f-1])
            listt=rotate(f,listt)

l=int(input())#6
f=int(input())#3
fun(l,f)#3642