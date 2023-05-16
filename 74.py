# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, numbers = int(input()), input().split()

print(all(int(number) > 0 for number in numbers) and any(number == number[::-1] for number in numbers))
