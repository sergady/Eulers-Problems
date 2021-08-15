# Find the difference between the sum of the squares of teh first one hundred natural numbers
# and the square of the sum

squareSum = 0
for i in range(101):
    squareSum += i
squareSum = squareSum**2
print(squareSum)

sumSquare = 0
for i in range(101):
    sumSquare += i**2
print(sumSquare)
print(squareSum - sumSquare)