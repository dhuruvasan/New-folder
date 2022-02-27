def is_palindrome(s):
    odd_counter = 0
    arr=[]
    for letter in s:
        if s.count(letter) % 2 != 0 and letter not in arr:
            odd_counter += 1
            arr.append(letter)

    if odd_counter > 1:
        return False
    return True

str=input().strip()
print(is_palindrome(str))