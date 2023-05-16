# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy


row, col = map(int, input().split(" "))
array = numpy.array([input().split() for _ in range(row)], int)

print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(round(numpy.std(array), 11))
