n=5
for i in range(1,n):
    print(i)
    for j in range(n):
        if i==j:
            print(n+(i-j),end="")
    print("")