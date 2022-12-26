def count_specialcharacter(s):
    temp_specialcharacter=0
    for i in s:
        if i  not in 'ASWEDRFTGYHUJIKOLPMNBVCXZsaswertyuiopsdfghjklmnbvcxz0123456789':
            temp_specialcharacter+=i
    return temp_specialcharacter
str1=input()
a=count_specialcharacter(str1)
print("no of specialcharacters in:'",str1,"'is",a)
