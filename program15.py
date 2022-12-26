def extract_consonants(s):
    temp_consonants=''
    for i in s:
        if i in 'DFKHGJKDNVJBKLDFkjdlkghdkjln':
            temp_consonants+=i
    return temp_consonants
str1=input()
a=extract_consonants(str1)
print("consonants;",a)
