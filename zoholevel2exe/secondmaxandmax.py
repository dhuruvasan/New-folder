# A-3 Write a function that takes an array of integers as input and prints the second-maximum difference
# between any two elements from an array.
# Example:
# int an-(14, 12, 70, 15, 95, 65, 22 , 30},
# First max-difference = 95-12-83
# Second max-difference = 95 -14 = 81
# So output should be 81

def fun(arr):
    rrn=[]
    for i in arr:
        if i not in rrn:
            rrn.append(i)
    rrn.sort()
    mi=rrn[1]
    mx=max(rrn)
    ans=mx-mi
    print(ans)

arr=[14, 12, 70, 15, 95,95,45,18,14,13 ,65, 22 , 30]
fun(arr)
