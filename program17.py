def extract_specialcharacter(s):
    temp_specialcharacter=''
    for i in s:
        if i  not in 'ASWEDRFTGYHUJIKOLPMNBVCXZsaswertyuiopsdfghjklmnbvcxz0123456789':
            temp_specialcharacter+=i
    return temp_specialcharacter
str1=input()
a=extract_specialcharacter(str1)
print("specialcharacter;",a)
