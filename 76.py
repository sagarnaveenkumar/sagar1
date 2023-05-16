# Enter your code here. Read input from STDIN. Print output to STDOUT
#finding float value is true or false
t=int(input())
k=[]
for i in range(t):
    n=input()
    c=n.count('.')

    if c==1:
        
        ind=n.index('.')
        if n[-1]=='.' or n.isalnum() or n.isalpha() or '.' not in n or '-+' in n or '+-' in n: #return False
            k.append(False)
        elif (n[0]=='+' or n[0]=='-') and n[1:ind].isdigit() and n[ind+1:].isdigit():
            
            k.append(True)
        elif n[0]=='.' and n[1:].isdigit():
            k.append(True)
        elif (n[0]=='+' or n[0]=='-') and n[1]=='.' and n[2:].isdigit():
           k.append(True)
        elif n[0].isdigit() and n[:-1].isdigit():
           k.append(True)
        elif n[0].isdigit() and n[ind+1:].isdigit() and n[:ind].isdigit():
            k.append(True)
        else:
            k.append(False)
    else:
        k.append(False)
for j in k:
    print(j)
