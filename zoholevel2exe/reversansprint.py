def reverses(st):
    # Mark spaces in result
    n = len(st)
    print(n)
    result = [0] * n
    print(result)
    for i in range(n):
        if (st[i] == ' '):
            result[i] = ' '
    print(result)
    # Traverse input string from beginning
    # and put characters in result from end
    j = n - 1
    print(j)
    for i in range(len(st)):
        # Ignore spaces in input string
        if (st[i] != ' '):
            print(st[i])
            # Ignore spaces in result.
            if (result[j] == ' '):
                j -= 1
            result[j] = st[i]
            j -= 1
    return ''.join(result)

# Driver code
if __name__ == "__main__":

    st = "go zoho"
    print(reverses(st))

# This code is contributed by ukasp













# def fun(str):
#     arr=[]len(str)
#     for i in range(len(str)):
#         if(str[i]==" "):
#             arr[i]="l"
#     k=str[::-1]
#     k=k.replace(" ","")
#     for j in range(len(k)):
#         if arr[j]!="l":
#             arr[j]=k[j]
#     print(arr)


# str="GoZO HO"
# fun(str)