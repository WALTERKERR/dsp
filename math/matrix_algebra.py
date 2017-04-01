# Matrix Algebra



import numpy
from numpy import matrix

a = matrix([[1,2,3],[2,7,4]])
b = matrix([[1,-1],[0,1]])
c = matrix([[5,-1],[9,1],[6,0]])
d = matrix([[3,-2,-1],[1,2,3]])
u = matrix([[6,2,-3,5]])
v = matrix([[3,5,-1,4]])
w = matrix([[1],[8],[0],[5]])
x = 6

a.shape  # 1.1) 2 x 3
b.shape  # 1.2) 2 x 2
c.shape  # 1.3) 3 x 2
d.shape  # 1.4) 2 x 3
u.shape  # 1.5) 1 x 4
w.shape  # 1.6) 4 x 1

#2.1
#In [36]: u + v
#Out[36]: matrix([[ 9,  7, -4,  9]])

#2.2
#In [37]: u - v
#Out[37]: matrix([[ 3, -3, -2,  1]])

#2.3
# In [39]: 6 * u
# Out[39]: matrix([[ 36,  12, -18,  30]])

#2.4
# In [44]: numpy.dot( numpy.array(u)[:,0], v)
# Out[44]: matrix([[18, 30, -6, 24]])

#2.5
# In [46]: numpy.linalg.norm(u)
# Out[46]: 8.6023252670426267

#3.1
# undefined
# In [47]: a + c
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-47-ca57d551b7f3> in <module>()
# ----> 1 a + c

# ValueError: operands could not be broadcast together with shapes (2,3) (3,2)

#3.2
# In [51]: a - c.T
# Out[51]:
# matrix([[-4, -7, -3],
#         [ 3,  6,  4]])

# 3.3
# In [54]: c.T + (3*(d))
# Out[54]:
# matrix([[14,  3,  3],
#         [ 2,  7,  9]])

# 3.4
# In [55]: b * a
# Out[55]:
# matrix([[-1, -5, -1],
#         [ 2,  7,  4]])

# 3.5
# undefined
# In [56]: b * a.T
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-56-06308bd4d84b> in <module>()
# ----> 1 b * a.T

# /anaconda/lib/python3.6/site-packages/numpy/matrixlib/defmatrix.py in __mul__(self, other)
#     341         if isinstance(other, (N.ndarray, list, tuple)) :
#     342             # This promotes 1-D vectors to row vectors
# --> 343             return N.dot(self, asmatrix(other))
#     344         if isscalar(other) or not hasattr(other, '__rmul__') :
#     345             return N.dot(self, other)

# ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

# Optional
# 3.6
# undefined
# ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

# 3.7
# In [58]: c * b
# Out[58]:
# matrix([[ 5, -6],
#         [ 9, -8],
#         [ 6, -6]])

# 3.8
# In [59]: b**4
# Out[59]:
# matrix([[ 1, -4],
#         [ 0,  1]])

# 3.9
# In [60]: a*a.T
# Out[60]:
# matrix([[14, 28],
#         [28, 69]])

# 3.10
# In [61]: d.T * d
# Out[61]:
# matrix([[10, -4,  0],
#         [-4,  8,  8],
#         [ 0,  8, 10]])

