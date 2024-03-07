#!/bin/python3

import math
import os
import random
import re
import sys

def gridChallenge(grid):
    if not grid or not grid[0]:
        return "YES"  # หาก grid ว่างหรือไม่มีคอลัมน์เลย จะถือว่าเรียงลำดับแล้ว

    # วนลูปผ่านทุกแถวของ grid
    for i in range(len(grid)):
        # เรียงลำดับตัวอักษรในแต่ละแถว
        grid[i] = ''.join(sorted(grid[i]))

    # ตรวจสอบว่าแต่ละคอลัมน์เรียงลำดับเป็นลำดับไม่ลดลง
    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            # เปรียบเทียบตัวอักษรในคอลัมน์ปัจจุบันสำหรับแต่ละแถว
            if grid[i][j] < grid[i - 1][j]:
                return "NO"

    # ถ้าทุกเงื่อนไขถูกต้อง แสดงว่า grid เรียงลำดับแล้ว
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ.get('OUTPUT_PATH', 'default_output.txt'), 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
