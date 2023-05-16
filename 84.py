# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


func = lambda x: "and" if x.group(0) == "&&" else "or"
pattern = re.compile(r'(?<=\s)(?:&&|\|\|)(?=\s)')
print(*[re.sub(pattern, func, input()) for _ in range(int(input()))], sep="\n")
