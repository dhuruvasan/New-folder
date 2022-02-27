def fun(n):
    strr=""
    k=97
    l=1
    for i in range(0,n):
        print(len(strr),n)
        num=len(strr)
        if num<n:
            strr=strr+chr(k)
            k+=1
            strr=strr+str(l)
            l=l+1
    print(strr[:n-1])


n=9
fun(n)