#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem
import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Make an array of 0s from 0 to arrRange
    tallyArray = [0] * 100
    # tallyArray = [i*0 for i in range(0, arrRange+2)] # Plus two for boundaries
    for i in range(len(arr)):
        tallyArray[arr[i]] += 1
    return tallyArray
