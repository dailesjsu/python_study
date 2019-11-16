#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
import os
import random
import re
import sys

def diagonalDifference(arr):
    sum1=0
    sum2=0
    for i in range(0,n):
       for j in range(0,n):
            if i==j:
               sum1=sum1+arr[i][j]
            if i== n - j - 1:
                sum2=sum2+arr[i][j]
    print(abs(sum1-sum2))


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
