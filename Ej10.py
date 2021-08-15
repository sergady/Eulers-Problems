# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
# True if prime
# False if not prime
def isPrime(num):
    if(num == 2):
        return True

    i = 2
    while num%i !=0:
        if(i >= int(math.sqrt(num))):
            return True
        i += 1
    
    return False

sum = 0
for i in range(2,2000001):
    if(isPrime(i)):
        sum += i

print(sum)