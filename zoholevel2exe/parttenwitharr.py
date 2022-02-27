def fun(str):
    n=len(str)
    k=int(len(str)/2)
    l=str[k:]+str[:k]
    lm=0
    for i in range(0,n):
        for j in range(i+1,n):
          print(" ",end="")
        for m in range(j,n):
            print(l[:lm+1],end="")
            lm=lm+1
        print("")
str=input()
fun(str)