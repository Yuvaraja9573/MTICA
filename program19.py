def extract_digits(s):
    temp_digits=''
    for i in s:
        if i in '1234567890':
            temp_digits+=i
    return temp_digits
str1=input()
a=extract_digits(str1)
print("digits;",a)
