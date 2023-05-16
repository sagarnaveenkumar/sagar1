# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    for i in range(int(input())):
        a=input()
        if len(a)==10 and a.isnumeric()==True and int(a[0]) in [7,8,9]:print("YES")
        else:print("NO")
