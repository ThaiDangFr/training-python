def prime_numbers(n):
    r = n
    lst = []
    isprime = True
    for i in range(2,n):
        if r % i == 0:
            lst.append(i)
            r = r // i
            lst += prime_numbers(r)
            isprime = False
            break

    if isprime:
        lst.append(n)
        
    return lst


def is_prime(n):
    isprime = True
    for i in range(2,n):
        if n % i == 0:
            isprime = False
            break
    return isprime

print(is_prime(5))
print(is_prime(15))  
print(prime_numbers(20))
