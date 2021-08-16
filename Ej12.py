# What is the value of the first triangle number to have over five hundred divisors?

def sumNatural(num):
    return (num+1) * num/2

def findFactors(num):
    i = 1
    factors = 1 # the number itself 
    while i <= num//2:
        if(num % i == 0):
            factors +=1
        i += 1
    return factors



print(findFactors(sumNatural(76576500)))