def isprime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
    
def filter_prime(numbers):
    return list(filter(isprime,numbers))

numbers_str=input("enter list of numbers:")
numbers_list=(list(map(int,numbers_str.split())))

prime_numbers=filter_prime(numbers_list)
print("prime numbers:",prime_numbers)
