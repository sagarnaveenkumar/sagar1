def minion_game(string):
    # your code goes heredef minion_game(string):
    s=k=0
    vowels=['A','E','I','O','U']
    for i in range(len(string)):
        if string[i] in vowels:
            k+=len(string[i:])
        else:
            s+=len(string[i:])
    if s > k :
        print('Stuart',s)
    elif k>s:
        print('Kevin',k)
    else:
        print('Draw')


