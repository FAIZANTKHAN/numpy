Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a=np.array([5,6,9])
a[0]
5
>>> a[1]
6
>>> a=np.array([1,2],[3,4],[5,6])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=np.array([1,2],[3,4],[5,6])
TypeError: array() takes from 1 to 2 positional arguments but 3 were given
>>> a=np.array([[1,2],[3,4],[5,6]])
>>> a.ndim
2
>>> a.itemsize
4
>>> a.dtype
dtype('int32')
>>> a.size
6
>>> a.shape
(3, 2)
>>> a=np.array([[1,2],[3,4],[5,6]],dtype=complex)
>>> a
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j],
       [5.+0.j, 6.+0.j]])
>>> hp.zeros((3,4))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    hp.zeros((3,4))
NameError: name 'hp' is not defined. Did you mean: 'np'?
>>> hp.zeros(3,4)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    hp.zeros(3,4)
NameError: name 'hp' is not defined. Did you mean: 'np'?
>>> np.zeros((3,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.ones((3,4))
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> l=range(0,5)
>>> l
range(0, 5)
>>> np.arange(1,5)
array([1, 2, 3, 4])
np.arange(1,5,2)
array([1, 3])
np.linspace(1,5,10)
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
a=np.array([[1,2],[3,4],[5,6]])
a
array([[1, 2],
       [3, 4],
       [5, 6]])
a.shape
(3, 2)
a.reshape(2,3)
array([[1, 2, 3],
       [4, 5, 6]])
a.min()
1
a.max()
6
a.sum()
21
a.sum(axis=0)
array([ 9, 12])
a.sum(axis=1)
array([ 3,  7, 11])
np.sqrt(a)
array([[1.        , 1.41421356],
       [1.73205081, 2.        ],
       [2.23606798, 2.44948974]])
np.std(a)
1.707825127659933
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
a+b
array([[ 6,  8],
       [10, 12]])
a*b
array([[ 5, 12],
       [21, 32]])
a/b
array([[0.2       , 0.33333333],
       [0.42857143, 0.5       ]])
a.dot(b)
array([[19, 22],
       [43, 50]])
