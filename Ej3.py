import math
# The prime factors of 13195 are 5, 7, 13 and 29.  
# What is the largest prime factor of the number 600851475143?
number = 600851475143
numberSq = int(math.sqrt(number))

def isPrime(num):
    if(num == 2):
        return True

    i = 2
    while num%i !=0:
        if(i >= int(math.sqrt(num))):
            return True
        i += 1
    
    return False

while numberSq > 0:
    if isPrime(numberSq) and number % numberSq == 0:
        print(numberSq)
        break
    else:
        numberSq -= 1