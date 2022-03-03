"""
Given a number n as input, calculate the sum of squares of first n numbers. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> 4
Output-> 30
"""

def recur(n):
  if (n==1):
    return 1
  else:
    return ((n*n) + recur(n-1))

n=4
print(recur(n))