Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> n=[6,7,8]
>>> n[0:2]
[6, 7]
>>> n[-1]
8
>>> a=np.array([6,7,8])
>>> a[o:2]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[o:2]
NameError: name 'o' is not defined
>>> a[0:2]
array([6, 7])
>>> a[-1]
8
>>> #Both list and numpy array have same kind of indexing
>>> a=np.array([[6,7,8],[1,2,3],[9,3,2]])
>>> a
array([[6, 7, 8],
       [1, 2, 3],
       [9, 3, 2]])
>>> a[1,2]
3
>>> a[0:2,2]
array([8, 3])
>>> a[0:1,1]
array([7])
>>> a[-1]
array([9, 3, 2])
>>> a[-1,0:2]
array([9, 3])
>>> a[-1,0:1]
array([9])
>>> a[:,1:3]
array([[7, 8],
       [2, 3],
       [3, 2]])
>>> #Indexing and Slicing complete
>>> 
>>> 
>>> 
>>> #Iterating through array
>>> a=np.array([6,7,8],[1,2,3],[9,3,2]])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
a=np.array([[6,7,8],[1,2,3],[9,3,2]])
a
array([[6, 7, 8],
       [1, 2, 3],
       [9, 3, 2]])
for row in a
SyntaxError: incomplete input
for row in a:
    print(row)

[6 7 8]
[1 2 3]
[9 3 2]
for cell in a.flat:
    print(cell)

6
7
8
1
2
3
9
3
2
#stacking two array together
a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)
a
array([[0, 1],
       [2, 3],
       [4, 5]])
b
array([[ 6,  7],
       [ 8,  9],
       [10, 11]])
np.vstack((a,b))
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11]])
np.hstack((a,b))
array([[ 0,  1,  6,  7],
       [ 2,  3,  8,  9],
       [ 4,  5, 10, 11]])
np.hsplit(a,3)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    np.hsplit(a,3)
  File "C:\Users\Faizan\AppData\Local\Programs\Python\Python312\Lib\site-packages\numpy\lib\shape_base.py", line 938, in hsplit
    return split(ary, indices_or_sections, 1)
  File "C:\Users\Faizan\AppData\Local\Programs\Python\Python312\Lib\site-packages\numpy\lib\shape_base.py", line 864, in split
    raise ValueError(
ValueError: array split does not result in an equal division
a=np.arange(12).reshape(3,4)
a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
