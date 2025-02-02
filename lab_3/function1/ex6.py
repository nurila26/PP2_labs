def reversion(word):
    word=list(word.split())
    word.reverse()
    for i in word:
        print(i,end=" ")

word=str(input("word:"))
reversion(word)