# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

pol = list(map(float, input().split()))

print(numpy.polyval(pol, int(input())))
