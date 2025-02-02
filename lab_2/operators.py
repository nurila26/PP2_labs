#Python Arithmetic Operators
print(10 + 5) #addition 
print(10 - 5) #substraction
print(10 * 5) #multiplication
print(10 / 5) #division
print(10 % 5) #modulus
print(10 ** 5) #Exponentiation
print(10 // 5) #Floor division

#Python Assignment Operators
x = 5
x+=3
x-=3
x*=3
x/=3
x%=3
x//=3
x**=3 
x&=3 #and (x=5 binary x=0101  binary 3=0011  0101 and 0011 =0001=1)
x|=3 #or  (x=5 binary x=0101  binary 3=0011  0101 and 0011 =0001=1)
x^=3 #XOR (x=5 binary x=0101  binary 3=0011  0101 and 0011 =0110=6)
x >>= 3  #(x=5 binary x=0101(4 bits)  shift rifht for 3 bits  0101=0000=0)
x <<= 3  #(x=5 binary x=0101(4 bits)  shift left for 3 bits  0101=0101000=40)
print(x := 3) #x = 3 print(x)

#Python Comparison Operators
"""
= equal
!= not equal
> greater than
< less than
>= Greater than or equal to
<= less than or equal to
"""

#Python Logical Operators
"""
and Returns True if both statements are true x < 5 and  x < 10
or  Returns True if one of the statements is true x < 5 or x < 4
not Reverse the result, returns False if the result is true not(x < 5 and x < 10)
"""

#Python Identity Operators
"""
is Returns True if both variables are the same object x is y
is not  Returns True if both variables are not the same object x is not y
"""

#Python Membership Operators
"""
in Returns True if a sequence with the specified value is present in the object x in y 
not in  Returns True if a sequence with the specified value is not present in the object x not in y
"""

#Python Bitwise Operators
"""
& and
| or
^ xor
~ not
<< Zero fill left shift
>>  Signed right shift"""