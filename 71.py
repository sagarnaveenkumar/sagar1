# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())
polynomials = input().split('+')
result = sum(eval(poly) for poly in polynomials[:k])
print('True' if result == k else 'False')
