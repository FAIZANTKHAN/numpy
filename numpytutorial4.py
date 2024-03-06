Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a=
a=np.arange(12).reshape(3,4)
a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
for row in a:
    print(row)

[0 1 2 3]
[4 5 6 7]
[ 8  9 10 11]
for cell in a.flatten:
    print(cell)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    for cell in a.flatten:
TypeError: 'builtin_function_or_method' object is not iterable
for cell in a.flatten():
    print(cell)

0
1
2
3
4
5
6
7
8
9
10
11
for x in np.nditer(a,order='c')
SyntaxError: incomplete input
>>> for x in np.nditer(a,order='c'):
...     print(x)
... 
0
1
2
3
4
5
6
7
8
9
10
11
>>> for x in np.nditer(a,order='f'):
...     print(x)
... 
0
4
8
1
5
9
2
6
10
3
7
11
>>> for x in np.nditer(a,order='f',flags=[external-loop]):
...     print(x)
... 
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for x in np.nditer(a,order='f',flags=[external-loop]):
NameError: name 'external' is not defined
>>> for x in np.nditer(a,order='f',flags=['external-loop']):
...     print(x)
... 
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for x in np.nditer(a,order='f',flags=['external-loop']):
ValueError: Unexpected iterator global flag "external-loop"

