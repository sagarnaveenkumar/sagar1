# Enter your code here. Read input from STDIN. Print output to STDOUT
def score_words(words ,vow = 'aeiouy'):
    score = 0
    for word in words.split():
        total = len([w for w in word if w in vow])
        if total%2: score += 1
        else: score += 2
    return score

N, words = int(input()), input()
print(score_words(words))
