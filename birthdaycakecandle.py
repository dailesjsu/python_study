You are in charge of the cake for your niece's birthday and 
have decided the cake will have one candle for each year of her total age. When she blows out the candles, 
she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    #numbers = map(int, ar)
    sort=sorted(ar)
    count=0
    for i in range(len(sort)):
        if sort[i]==sort[-1]:
            count=count+1
    print(count)
            
if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
