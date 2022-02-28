# • Given two strings s1 and s2, write a function that will convert s1 to
# s2(if possible) by using only one operation.
# • Example
# • INPUT
# s1 = "abcd"
# s2 = "cbad"
# OUTPUT
# 2
# The number of opeartions took are 2
# • Explanation
# Pick 'b' and insert it at beginning ie, "abcd" -> “bacd"
# Pick 'c' and insert it at beginning ie, “bacd" -> “cbad"


def Fun(s1,s2):
    l=0
    if(len(s1)==len(s2)):
        k=0
        for i in s1:
            if i in s2:
                k=k+1
        if(k==len(s1)):
            l=1
    if(l==1):
        i=len(s1)-1
        ans=0
        for i in range(i,0,-1):
            j=i
            while (i>=0 and s1[i] != s2[j]):
                i-=1
                ans+=1
            if (i >= 0):
                i-=1
                j-=1
        return ans


s1=input()
s2=input()
print(Fun(s1,s2))