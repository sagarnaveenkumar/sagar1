# Enter your code here. Read input from STDIN. Print output to STDOUT
n=map(int,input())
enroll_english=set(map(int,input().split()))
b=map(int,input())
enroll_french=set(map(int,input().split()))
eng_or_french=enroll_english.symmetric_difference(enroll_french)
print(len(eng_or_french))
