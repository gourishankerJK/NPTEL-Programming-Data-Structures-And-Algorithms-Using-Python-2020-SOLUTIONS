'''Write a function contracting(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly decreases.

Here are some examples of how your function should work.

  >>> contracting([9,2,7,3,1])
  True

  >>> contracting([-2,3,7,2,-1])
  False

  >>> contracting([10,7,4,1])
  False
In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than its neighbours and a valley if it is strictly less than its neighbours.
Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] where hc is the number of hills in l and vc is the number of valleys in l.

Here are some examples to show how your function should work.


>>> counthv([1,2,1,2,3,2,1])
[2, 1]

>>> counthv([1,2,3,1])
[1, 0]

>>> counthv([3,1,2,3])
[0, 1]

A square n×n matrix of integers can be written in Python as a list with n elements, where each element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix

  1  2  3
  4  5  6
  7  8  9
would be represented as [[1,2,3], [4,5,6], [7,8,9]].

Write a function leftrotate(m) that takes a list representation m of a square matrix as input, and returns the matrix obtained by rotating the original matrix counterclockwize by 90 degrees. For instance, if we rotate the matrix above, we get

  3  6  9
  2  5  8
  1  4  7
Your function should not modify the argument m provided to the function rotate().

Here are some examples of how your function should work.


  >>> leftrotate([[1,2],[3,4]])
  [[2, 4], [1, 3]]

  >>> leftrotate([[1,2,3],[4,5,6],[7,8,9]])
  [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

  >>> leftrotate([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]] '''


def contracting(l):
    min = abs(l[1] - l[0])
    for i in range(2, len(l)):
        if min <= abs(l[i] - l[i - 1]):
            return False
        min = abs(l[i] - l[i - 1])
    return True


def counthv(l):
    count = [0, 0]
    for i in range(1, len(l) - 1):
        if l[i - 1] > l[i] < l[i + 1]:
            count[1] += 1
        elif l[i - 1] < l[i] > l[i + 1]:
            count[0] += 1
    return count


def leftrotate(m):
    n = len(m)
    larr = [[0] * n for _ in range(n)]
    k = 0
    for j in range(n - 1, -1, -1):
        for i in range(n):
            larr[k][i] = m[i][j]
        k += 1
    return larr
