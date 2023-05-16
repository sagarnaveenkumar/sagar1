# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

inputs = [input() for _ in range(int(input()))]
mpl = [r'[A-Z].*[A-Z]', r'\d.*\d.*\d', r'^[a-zA-Z0-9]{10}$']  # must patterns list
mnp = r'([a-zA-Z0-9]).*\1'  # must not pattern
result = [all(re.search(p, i) for p in mpl) and not re.search(mnp, i) for i in inputs]
print(*["Valid" if x else "Invalid" for x in result], sep="\n")
