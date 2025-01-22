#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    runningTallyOfNumbers = {
        "positive": 0,
        "negative": 0,
        "zero": 0
    }
    for number in arr:
        if number < 0:
            runningTallyOfNumbers["negative"] += 1
        elif number > 0:
            runningTallyOfNumbers["positive"] += 1
        else:
            runningTallyOfNumbers["zero"] += 1
    print(runningTallyOfNumbers["positive"] / len(arr))
    print(runningTallyOfNumbers["negative"] / len(arr))
    print(runningTallyOfNumbers["zero"] / len(arr))
