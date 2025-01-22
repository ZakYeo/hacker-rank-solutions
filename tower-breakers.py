#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/problem
import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def towerBreakers(n, m):
    if m == 1:
        return 2
    else:
        return 1 if n % 2 == 1 else 2
