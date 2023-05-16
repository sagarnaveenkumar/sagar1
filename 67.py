# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set(map(int, input().split()))
flag = True
for _ in range(int(input())):
    set_n = set(map(int, input().split()))
    if not set_A.issuperset(set_n):
        flag = False
print(flag)
