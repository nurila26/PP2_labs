def palindrom(word):
    if word==word[::-1]:
        print("YES")
    else:
        print("NO")

word = input("word: ")
palindrom(word)