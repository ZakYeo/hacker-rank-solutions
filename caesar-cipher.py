#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem
import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
alphabet = "abcdefghijklmnopqrstuvwxyz"


def calculateCipherDict(shift, alphabet):
    cipherDict = {}
    for index, letter in enumerate(alphabet):
        if index + shift > len(alphabet)-1:
            newIndex = (index + shift) % len(alphabet)
        else:
            newIndex = index + shift
        cipherDict[letter] = alphabet[newIndex]
        cipherDict[letter.upper()] = alphabet[newIndex].upper()

    return cipherDict


def caesarCipher(s, k):
    cipher = ""
    cipherDict = calculateCipherDict(k, alphabet)
    for letter in s:
        if letter not in alphabet and letter not in alphabet.upper():
            cipher += letter
        else:
            cipher += cipherDict[letter]
    return cipher
