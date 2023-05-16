# Enter your code here. Read input from STDIN. Print output to STDOUT
lenA = int(input())
setA = set(map(int, input().split(' ')))
otherSets = int(input())

for _ in range(otherSets):
    cmd = list(input().split(' '))
    refSet = set(map(int, input().split(' ')))
    
    if cmd[0] == "update":
        setA.update(refSet)
        #print(str(setA) + " - Upd")
        
    elif cmd[0] == "symmetric_difference_update":
        setA.symmetric_difference_update(refSet)
        #print(str(setA) + " - SymmDiffUpd")
        
    elif cmd[0] == "difference_update":
        setA.difference_update(refSet)
        #print(str(setA) + " - DiffUpd")
        
    elif cmd[0] == "intersection_update":
        setA.intersection_update(refSet)
        #print(str(setA) + " - IntersUpd")
        
    else:
        print("No valid command entered")
        
print(str(sum(setA)))
