#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#
stack = []
l1 = []
def getMax(operations):
    for i in operations:
        #print(i)
        if len(i)>2:
            #print("hi")
            x = i.split(" ")
            #print(x[1])
            stack.insert(0,int(x[1]))
            #print(stack)
        elif int(i) == 2:
            stack.pop(0)
        else:
            print(max(stack))
            l1.append(max(stack))
    print(l1)
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)


    res = getMax(ops)
##
##    fptr.write('\n'.join(map(str, res)))
##    fptr.write('\n')
##
##    fptr.close()
