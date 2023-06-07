#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s=s.lower()
    s=list(s)
    ln=len(s)
    s[0]=s[0].upper()
    for i in range(1,ln):
        if s[i-1]==" " and s[i]!=" ":
            s[i]=s[i].upper()
    r=''.join(s)
    return(r)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
