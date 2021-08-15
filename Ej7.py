# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
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

order = 0
numbers = 2
lastPrime = 2
while order < 10001:
    if(isPrime(numbers)):
        order +=1
        lastPrime = numbers
    numbers += 1

print(lastPrime)