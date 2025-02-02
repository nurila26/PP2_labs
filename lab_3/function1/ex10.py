def unique(list1):
    result=[]
    for i in list1:
        if list1.count(i)==1:
            result.append(i)
    return result

n=int(input("n:"))
list1=[]
for i in range(n):
    num=int(input("number:"))
    list1.append(num)
print(unique(list1))