import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
#print(matrix)
    
decoded_script=''

i=0
while i<m:   
    for a in matrix:
        decoded_script+=a[i]
    i+=1
#print(decoded_script)
pattern=r'([a-zA-Z0-9])[^(a-zA-Z0-9)]+([a-zA-Z0-9])'
final=re.sub(pattern,r'\1 \2',decoded_script)
print(final)
