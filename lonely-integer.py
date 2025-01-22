#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem
import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    # Convert the numbers into a string list
    arrayAsString = " ".join(str(itemInArray) for itemInArray in a)
    arrayAsArrayOfStrings = "".join(arrayAsString).split(" ")
    for item in arrayAsArrayOfStrings:
        if len(re.findall(item, arrayAsString)) == 1:
            return item
