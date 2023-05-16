# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

N = int(input())

A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)

print(numpy.dot(A,B))
