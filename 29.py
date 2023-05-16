def merge_the_tools(s, k):
    # your code goes here
    p = ""
    for i in range(len(s)):
            
        if s[i] in p:
            pass
            if (i+1)%k == 0:
                print(p)
                p=""
            
        else:
            p += s[i]
            if (i+1)%k == 0:
                print(p)
                p=""
