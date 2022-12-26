def count_consonants(s):
    n_consonants=0
    for i in s:
        if i in 'QWRTYPLKJHGFDSZXCVBNMqwrtyplkjhgfdsnmbvcxz':
            n_consonants+=1
    return n_consonants
str1=input()
a=count_consonants(str1)
print("no of consonantsin:'",str1,"'is",a)
    
