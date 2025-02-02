def howmany(numheads,numlegs):
    x=(4*numheads-numlegs)//2
    y=numheads-x
    return f"Chickens:{x}, Rabbits:{y}"
print(howmany(35,94))


"""x+y=35
2x+4y=94
y=35-x
2x+4(35-x)=94
2x+4*35-4x=94
-2x=94-4*35
x=(4*35-94)//2"""

    