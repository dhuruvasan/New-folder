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
    if(len(s1)==len(s2)):
        k=0
        for i in s1:
            if i in s2:
                k=k+1
        if(k==len(s1)):
            print(k)


s1=input()
s2=input()
Fun(s1,s2)