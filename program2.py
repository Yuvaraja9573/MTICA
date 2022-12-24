Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lst1=list()
type(lst1)
<class 'list'>
lst1.append(10)
lst1
[10]
lst1.append(15)
lst.append(10)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    lst.append(10)
NameError: name 'lst' is not defined. Did you mean: 'lst1'?
lst1.append(15)
lst1.append(10)
lst1
[10, 15, 15, 10]
lst1.append('python')
lst1
[10, 15, 15, 10, 'python']
lst1.clear()
lst1
[]
lst1=[10,15,10,'python']
lst.count(10)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    lst.count(10)
NameError: name 'lst' is not defined. Did you mean: 'lst1'?
lst1.count(10)
2
lst1.append('mca')
lst1
[10, 15, 10, 'python', 'mca']
lst1.count('mca')
1
lst1.count('python')
1
len(lst1)
5
lst2=lst1
lst1
[10, 15, 10, 'python', 'mca']
lst2
[10, 15, 10, 'python', 'mca']
lst3=lst1.copy()
print(id(lst1),id(lst3))
3013134856320 3013139387584
lst1
[10, 15, 10, 'python', 'mca']
lst2
[10, 15, 10, 'python', 'mca']
lst3
[10, 15, 10, 'python', 'mca']
lst3.append('java')
lst3
[10, 15, 10, 'python', 'mca', 'java']
lst2=lst2.copy()
print(id(lst2),id(lst2))
3013134859968 3013134859968
lst1.apepend('hello')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    lst1.apepend('hello')
AttributeError: 'list' object has no attribute 'apepend'. Did you mean: 'append'?
lst1.append('hello')
lst1
[10, 15, 10, 'python', 'mca', 'hello']
lst3.append(10)
lst3
[10, 15, 10, 'python', 'mca', 'java', 10]
lst1
[10, 15, 10, 'python', 'mca', 'hello']
lst1[:]
[10, 15, 10, 'python', 'mca', 'hello']
lst1.append([11,22])
lst1
[10, 15, 10, 'python', 'mca', 'hello', [11, 22]]
lstt1[-1]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    lstt1[-1]
NameError: name 'lstt1' is not defined. Did you mean: 'lst1'?
lst1[-1]
[11, 22]
lst1.append(('c','c++','java','python'))
lst1
[10, 15, 10, 'python', 'mca', 'hello', [11, 22], ('c', 'c++', 'java', 'python')]
del lst1[3:5]
lst1
[10, 15, 10, 'hello', [11, 22], ('c', 'c++', 'java', 'python')]
lst1.extend
<built-in method extend of list object at 0x000002BD8CD53080>





lst1.extend([11,22])
lst1
[10, 15, 10, 'hello', [11, 22], ('c', 'c++', 'java', 'python'), 11, 22]
lst1.extend(('c','c++','java','python'))
lst1
[10, 15, 10, 'hello', [11, 22], ('c', 'c++', 'java', 'python'), 11, 22, 'c', 'c++', 'java', 'python']
lst1.index('c')
8
lst1.index(10)
0
lst1.index('java')
10
lst1.insert(0,'yuvaraj')
lst1
['yuvaraj', 10, 15, 10, 'hello', [11, 22], ('c', 'c++', 'java', 'python'), 11, 22, 'c', 'c++', 'java', 'python']
lst1.insert(30,'raj')
lst1
['yuvaraj', 10, 15, 10, 'hello', [11, 22], ('c', 'c++', 'java', 'python'), 11, 22, 'c', 'c++', 'java', 'python', 'raj']
lst1.index('raj')
13
lst1.index('c',2)
9
lst1.pop()
'raj'
lst1.pop('python')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    lst1.pop('python')
TypeError: 'str' object cannot be interpreted as an integer
lst1
['yuvaraj', 10, 15, 10, 'hello', [11, 22], ('c', 'c++', 'java', 'python'), 11, 22, 'c', 'c++', 'java', 'python']
a=lst1.pop()
a
'python'
b=lst1.pop()
b
'java'
e=lst1.pop()
e
'c++'
lst1
['yuvaraj', 10, 15, 10, 'hello', [11, 22], ('c', 'c++', 'java', 'python'), 11, 22, 'c']
a=lst1.pop(4)
a
'hello'
a=lst1.pop(9)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a=lst1.pop(9)
IndexError: pop index out of range
a=lst1.pop(6)
a
11
b=[]
b
[]
lst1
['yuvaraj', 10, 15, 10, [11, 22], ('c', 'c++', 'java', 'python'), 22, 'c']
a=list.pop(6)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a=list.pop(6)
TypeError: descriptor 'pop' for 'list' objects doesn't apply to a 'int' object
a=lst1.pop(6)
a
22
a=lst1.pop(6)
a
'c'
lst1.append('raj')
lst1
['yuvaraj', 10, 15, 10, [11, 22], ('c', 'c++', 'java', 'python'), 'raj']
lst1.remove('raj')
lst1
['yuvaraj', 10, 15, 10, [11, 22], ('c', 'c++', 'java', 'python')]
lst1.reverse()
lst1
[('c', 'c++', 'java', 'python'), [11, 22], 10, 15, 10, 'yuvaraj']
l1=[34,21,5.9,89,56,23]
l2=['yuvaraj','meghana','raj','maggi']
l1
[34, 21, 5.9, 89, 56, 23]
l1.sort()
l1
[5.9, 21, 23, 34, 56, 89]
l1.sort(reverse=True)
l1
[89, 56, 34, 23, 21, 5.9]
l2=.sort(reverse=true)
SyntaxError: invalid syntax
l2=sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    l2=sort(reverse=True)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
l2.sort(reverse=True)
l2
['yuvaraj', 'raj', 'meghana', 'maggi']
