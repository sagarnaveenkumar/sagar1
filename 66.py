# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
l = dict(Counter(input().split()))
print(*[x for x in l if l[x]!=k])
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    input()
    a = set(input().split())
    input()
    b = set(input().split())
    print(a.issubset(b))
