#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    result = ""

    for char in s:
        if char.isalpha():  # Check if the character is an alphabet
            # Determine whether it is an uppercase or lowercase letter
            if char.isupper():
                result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            result += char

    return result

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'default_output.txt'), 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
