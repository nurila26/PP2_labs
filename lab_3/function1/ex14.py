#фуекция прокерки на простое число
def isprime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
print(isprime(9))


#reverse words
def reversion(word):
    word=list(word.split())
    word.reverse()
    for i in word:
        print(i,end=" ")

reversion("My name is")