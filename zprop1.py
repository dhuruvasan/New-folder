def encode(st): 
    n = len(st)
    i = 0
    strr=''
    while i < n- 1:
        count = 1
        while (i < n - 1 and st[i] == st[i + 1]):
            count += 1
            i += 1
        i += 1
        
        strr+=st[i - 1] + f'{count}'
    return strr


if __name__=='__main__':
    t=int(input())
    arr=''
    for i in range(t):
        arr+=input().strip()
    print (encode(arr))
