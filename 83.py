# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
k = input()
lens = 0
   
if k in S:
    for i in range(len(S)):
        if S[i] == k[0]:
            for j in range(len(k)):
                if (i+j) > (len(S)-1):
                    break
                else:
                    if S[i+j] == k[j]:
                        lens += 1
                    else: lens = 0
            if lens == len(k):
                tup = (i,(len(k)+i-1))
                print(tup)
            lens = 0;
else:
    print((-1,-1))
