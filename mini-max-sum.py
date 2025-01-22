#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    print(str(sum(sorted(arr)[0:4])) + " " + str(sum(sorted(arr)[-4:])))
