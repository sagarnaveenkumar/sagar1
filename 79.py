# Enter your code here. Read input from STDIN. Print output to STDOUT
s = str(input())

found = False
for i in range(len(s)-1):
    if s[i].isalnum():
        if s[i] == s[i+1]:
            found = True
            print(s[i])
            break
if not found:
    print(-1)
