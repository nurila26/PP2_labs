def square_generator(N):
    for num in range(N + 1):
        yield num ** 2


N=int(input("N:")) 
for square in square_generator(N):
    print(square)

    