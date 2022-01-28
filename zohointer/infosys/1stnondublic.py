from re import L


def nondub(str):
    arr=[]
    for letter in str:
        if str.count(letter)==1:
            arr.append(letter)
    if not arr:
        print(-1)
    else:
        for i in range(len(str)):
            if str[i]==arr[0]:
                print(i+1)        


str=input().strip()
nondub(str)