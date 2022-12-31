Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict1={'Name': 'Zara','Age':7,'Class':'First'}
print(dict1)
{'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict1['Name'])
Zara
print(dict1['class'])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(dict1['class'])
KeyError: 'class'
print(dict1['Class'])
First
dict1['Age']=8
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Class': 'First'}
dict1['Course']='MCA'
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Class': 'First', 'Course': 'MCA'}
del dict1['Class']
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Course': 'MCA'}
dict1['Section']='A'
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Course': 'MCA', 'Section': 'A'}
dict1.clear()
print(dict1)
{}
dict1={'Name': 'Zara', 'Age': 8, 'Course': 'MCA', 'Section': 'A'}
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Course': 'MCA', 'Section': 'A'}
del dict1
print(dict1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(dict1)
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
dict1={'Name': 'Zara', 'Age': 8, 'Course': 'MCA', 'Section': 'A'}
dict1.keys()
dict_keys(['Name', 'Age', 'Course', 'Section'])
dict1.values()
dict_values(['Zara', 8, 'MCA', 'A'])
dict1.items()
dict_items([('Name', 'Zara'), ('Age', 8), ('Course', 'MCA'), ('Section', 'A')])
for i in dict1:print(i)

Name
Age
Course
Section
for i in dict1.keys():print(i)

Name
Age
Course
Section
for i in dict1.items():print(i,j)

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    for i in dict1.items():print(i,j)
NameError: name 'j' is not defined
for i,j in dict1.items():print(i,j)

Name Zara
Age 8
Course MCA
Section A
