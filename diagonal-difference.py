#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def getSumOfDiagonal(direction, matrix):
    tally = 0
    if direction == "primary":
        for i in range(0, len(matrix[0])):
            tally += matrix[i][i]
    elif direction == "secondary":
        for i in range(0, len(arr)):
            tally += matrix[i][len(arr)-i-1]
    return tally


def diagonalDifference(arr):
    return abs(getSumOfDiagonal("primary", arr) - getSumOfDiagonal("secondary", arr))
