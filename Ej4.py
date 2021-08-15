# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(num):
    # modulos de 10 para darle la vuelta
    listNums = []
    originalNum = num
    while num > 0:
        listNums.append(num%10)
        num = num // 10
    
    secondNum = 0
    power = len(listNums)-1
    for i in listNums:
        secondNum += i * 10**power
        power -= 1 

    #print ( originalNum )
    #print ( secondNum )    
    return originalNum == secondNum

maxNum = 0
for i in range(100,1000):
    for j in range(100, 1000):
        result = i*j
        if isPalindrome(result):   
            if(result > maxNum):
                maxNum = result

print(maxNum)