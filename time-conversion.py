#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Remove AM / PM:
    newS = s[0:-2]
    if s[-2:] == "PM":
        # Convert the hour
        if s[0:2] != "12":
            newH = int(s[0:2]) + 12
            newS = str(newH) + newS[2:]
    else:
        # Dealing with AM
        if s[0:2] == "12":
            newH = "00"
            newS = str(newH) + newS[2:]
    return newS
