
def fun(strr):
    split_value = []
    tmp = ''
    for c in strr:
        if c == '.':
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value.append(tmp)
    print(split_value)
    for j in range(0,len(split_value)):
        if j==0:
            print(split_value[j],end="")
        elif j==1:
            print(".xyz.",end="")
        elif(j%2!=0 and j!=0 and j!=1 and j!=len(split_value)-1):
            print(".xyz.",end="")
        elif(j==len(split_value)-1 and j%2!=0):
            print(".xyz",end="")
        else:
            print(split_value[j],end="")

strr='I.love'
fun(strr)