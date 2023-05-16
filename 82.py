# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S=input()
#print(S)

m=re.findall(r'(?=([^AEIOUaeiou])([AEIOUaeiou]{2,})([^AEIOUaeiou]))',S)
#print(m)

if m:
    for _ in m:
        print(_[1])
else:
    print(-1)
