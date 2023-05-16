
def solve(s):
    names = s.split(" ")
    for i in range(len(names)):
        names[i] = names[i].capitalize()
    return " ".join(names)

