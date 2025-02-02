def permutation(str1):
    for i in range(len(str1)):
        if len(str1) == 1:
            return str1
        
    result = []
    for i in range(len(str1)):
        current = str1[i]
        remaining = str1[:i] + str1[i+1:]

        perms = permutation(remaining)

        for j in range (len(perms)):
            result.append(current + perms[j])
        
    return result

str1 = str(input("word:"))
print(permutation(str1))