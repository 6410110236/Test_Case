import math
import os
import random
import re
import sys

def funnyString(s):
    if len(s) <= 1:
        return "Funny"

    # Calculate the absolute differences of adjacent characters in the original string
    original_diff = [abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)]
    
    # Create the reversed string
    reversed_s = s[::-1]
    
    # Calculate the absolute differences of adjacent characters in the reversed string
    reversed_diff = [abs(ord(reversed_s[i]) - ord(reversed_s[i + 1])) for i in range(len(reversed_s) - 1)]
    
    # Check if the lists of differences are the same
    if original_diff == reversed_diff:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'default_output.txt'), 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
