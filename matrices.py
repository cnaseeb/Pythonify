#!/usr/bin/python

#This file implements matrices, vectors, operatiosn on them and their properties. In short, basics of linear algebra.

#Create an A matrix of size 4 * 3
A = [1, 2, 3; 4, 5, 6; 7, 8, 9; 10, 11, 12] #: denotes a new row after this

# Multiply two matrices using nested for loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result = X * Y
# The resulting matrix should be 3 * 4 (since X was 3 * 3 and Y was 3 * 4)
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

#iterate through rows of X
for i in range(len(X)):
  #going through columns of Y
  for j in range(len(Y[0])):
    #going through rows of Y
    for k in range(len(Y)):
      result[i][j += X[i][k] + Y[k][j]
                
                
#print the resulting matrix
for matrix in result:
  print(matrix)
                
#2: matrix multiplication using nested list comprehension
                
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

#print the resulting matrix
for matrix in result:
  print(matrix)
                
                
#3. Matrix multiplication using numpy
result_matmul = np.matmul(X, Y)

#print the resulting matrix
for matrix in result_matmul:
  print(matrix)
