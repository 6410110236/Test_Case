#!/bin/python3

import math
import os
import random
import re
import sys

def alternate(s):
    # If the string has only one character, the length is 1
    if len(set(s)) == 1:
        return 1

    max_length = 0

    for char1 in set(s):
        for char2 in set(s):
            if char1 != char2:
                filtered_str = ''.join(c for c in s if c == char1 or c == char2)
                
                # Check if the filtered string is alternating
                if len(set(filtered_str)) == 2 and all(filtered_str[i] != filtered_str[i + 1] for i in range(len(filtered_str) - 1)):
                    max_length = max(max_length, len(filtered_str))

    return max_length


if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'default_output.txt'), 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
