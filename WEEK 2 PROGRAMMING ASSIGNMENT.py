''' A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .

Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.

>>> primeproduct(6)
True

>>> primeproduct(188)
False

>>> primeproduct(202)
True
Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), and returns the string obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s

Here are some examples to show how your function should work.


>>> delchar("banana","b")
'anana'

>>> delchar("banana","a")
'bnn'

>>> delchar("banana","n")
'baaa'

>>> delchar("banana","an")
'banana'
Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first elment in l1, then the first element in l2, then the second element in l2, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

Here are some examples to show how your function should work.

>>> shuffle([0,2,4],[1,3,5])
[0, 1, 2, 3, 4, 5]

>>> shuffle([0,2,4],[1])
[0, 1, 2, 4]

>>> shuffle([0],[1,3,5])
[0, 1, 3, 5]'''


def shuffle(l1, l2):
    list1 = list()
    length = len(l1) if len(l1) > len(l2) else len(l2)
    for i in range(length):
        if i < len(l1) and i < len(l2):
            list1.append(l1[i])
            list1.append(l2[i])
        elif i < len(l1):
            list1.append(l1[i])
        elif i < len(l2):
            list1.append(l2[i])
    return list1


def delchar(s, c):
    if len(c) > 1:
        return s
    news = ""
    for i in s:
        if c == i:
            pass
        else:
            news += i
    return news

def isprime(n):
    if n%2 == 0 and n!=2 or n == 1:
        return False
    if n % 3 == 0 and n == 3:
        return True
    else :
        for i in range(3,((n+1)//2),2):
            if n % i == 0:
                return False
        return True

def primeproduct(n):
    for i in range(2,(n+2)//2):
        if n % i == 0 :
            if isprime(i) and isprime(n//i):
                return True
    return False
