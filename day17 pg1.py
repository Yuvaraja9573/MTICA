Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from random import *
random()
0.8993706080837367
random()
0.590386554741982
randint(10,20)
10
random()
0.24813694809804343
randint(10,20)
18
randint(10,20)
20
for i in range(100):
    print(randint(10,20),end=',')

    
19,13,19,12,16,14,10,16,12,19,12,15,17,17,15,15,14,15,17,17,10,17,20,11,12,19,20,19,18,14,19,13,16,20,17,11,15,20,18,19,18,20,19,10,18,10,14,15,14,15,11,10,13,19,20,12,18,17,12,14,20,10,11,11,10,17,10,14,20,14,15,18,14,10,12,15,13,16,18,19,11,14,10,16,10,10,15,17,12,19,18,11,17,12,18,11,20,14,14,11,

================================ RESTART: Shell ================================
import random
random()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    random()
TypeError: 'module' object is not callable

================================ RESTART: Shell ================================
import random
random.random()
0.7358581729107146

================================ RESTART: Shell ================================
import random as r
r.random()
0.7020298301289942
help(r.random)
Help on built-in function random:

random() method of random.Random instance
    random() -> x in the interval [0, 1).

r.randint(10,99)
93
help(r.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

help(r.uniform)
Help on method uniform in module random:

uniform(a, b) method of random.Random instance
    Get a random number in the range [a, b) or [a, b] depending on rounding.

r.uniform(10,100)
36.673869644305555
items=[1,2,3,4,5,6,7,8,9,10]
r.shuffle(items)
items
[7, 3, 1, 2, 6, 9, 8, 5, 4, 10]
a=[12,'papaya',45,7.8,'mango']
r.shuffle(a)
a
[7.8, 12, 'papaya', 'mango', 45]
r.shuffle(a)
a
['papaya', 12, 'mango', 45, 7.8]
r.shuffle(a)
a
['mango', 45, 7.8, 'papaya', 12]

====================================================== RESTART: Shell ======================================================
import random as r
items=[1,2,3,4,5,6,7,8,9,10]
x=r.sample(items,3)
x
[1, 6, 4]
x=r.sample(items,3)
x
[7, 4, 10]
x=r.sample(items,2)
x
[9, 2]
