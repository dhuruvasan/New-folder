def fun(patt,str):
    ans=""
    for i in patt:
        for j in str:
            if i in j:
                ans=ans+j
    print(ans)

patt="bxyzca"
str="abcabcabc"
fun(patt,str)