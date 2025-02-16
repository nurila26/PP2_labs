def divisibleby3and4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num


n=int(input("n:"))
for number in divisibleby3and4(n):
    print(number)
