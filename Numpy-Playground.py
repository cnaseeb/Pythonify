#!/usr/bin/env python

import numpy as np

a = np.arange(15).reshape(3, 5)

print (a)
a.shape

b = np.arange(15).reshape(5, 3)

print (b)

b.shape

a.ndim

b.ndim

a.dtype.name

b.dtype.name

a.size

b.size

type(a)

type(b)

c = np.array([6, 7, 8])

c

type(c)
