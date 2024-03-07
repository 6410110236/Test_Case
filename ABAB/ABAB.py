#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    # Initialize a variable to count deletions
    deletions = 0
    
    # Iterate through the characters of the string starting from the second character
    for i in range(1, len(s)):
        # If the current character is the same as the previous one, increment deletions
        if s[i] == s[i - 1]:
            deletions += 1
    
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'default_output.txt'), 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
