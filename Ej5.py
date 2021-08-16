# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def evenlyDivisible(num):
    for i in range(1, 21):
        if (num % i != 0):
            return False
    return True

found = False
i = 1
while not found:
    if(evenlyDivisible(i)):
        sol = i
        found = True
    i += 1

print(sol)