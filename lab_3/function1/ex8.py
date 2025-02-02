def order007(arr):
    result=[]
    for i in range(len(arr)):
        if(arr[i]==0 or arr[i]==7):
            result.append(arr[i])

    a=False
    for i in range(len(result)):
        if result[0]==result[1] and result[0]==0 and result[2]==7:
            a=True
    if a:
        print("True")
    else:
        print("False")

order007([1,2,4,0,0,5,7])
order007([1,0,2,4,0,5,7])
order007([1,7,2,0,4,5,0])