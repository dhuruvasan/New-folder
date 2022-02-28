def pattern(st, length):
     
    # i and j are the indexes of characters
    # to be displayed in the ith iteration
    # i = 0 initially and go upto length of
    # string
    # j = length of string initially
    # in each iteration of i, we increment
    # i and decrement j, we print character
    # only of k==i or k==j
    for i in range(length):
        j = length -1 - i
        for k in range(length):
            if (k == i or k == j):
                print(st[k],end="")
            else:
                print(" ",end="")
        print()
 
# driver code
if __name__ == "__main__":
   
    st = "geeksforgeeks"
    length = len(st)
    pattern(st, length)