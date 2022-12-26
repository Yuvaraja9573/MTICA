def palindrome(s1):
    if s1==s1:
        return 'it is a palindrome'
    else:
        return'it is not a palindrome'
inp=input().split()
print(palindromornot(inp[0]))
