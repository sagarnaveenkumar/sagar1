# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=="__main__":
    number_of_students, number_of_subjects = map(int,input().split(" "))
    students = {}
    for i in range (number_of_students):
        students[i]=[]
    
    for _ in range (number_of_subjects):
        scores = zip(map(float, input().split(" ")),students.keys())
        for i in scores:
            students[i[1]].append(i[0])
    
    for scores in students.values():
        print(sum(scores)/len(scores))
