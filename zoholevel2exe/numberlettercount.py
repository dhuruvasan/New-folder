# A-1 Implement the below function to print the count of numeric characters (0-9) in a given string and also
# print the count of remaining characters (Ignore the character cases, it can be lower or upper case)
# The function will tako 1 parameter which will be a String (or a character array) You do not have to write
# code to get the input parameter from the user
# Input raja1123labs Output='1'=2, '2'=1, 3=1, others= 8
# Input Buffet101 Output '1'=2, '0'=1, others= 6

def fun(strr):
    lis=["0","1","2","3","4","5","6","7","8","9"]
    arr=[]
    ans=0
    arr1=[]
    for i in strr:
        if i in lis:
            c=strr.count(i)
            m=str(i)
            k=str(c)
            l=str("'"+m+"'"+'='+k)
            l=str(l)
            arr.append(l)
        else:
            ans=ans+1
    for n in arr:
        if n not in arr1:
            arr1.append(n)
            print(n,end=", ")
    print('others=',ans)


strr=input()
fun(strr)