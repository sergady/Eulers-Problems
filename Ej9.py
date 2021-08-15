
def checkABC(a,b,c):
    return a+b+c == 1000

def checkFormula(a,b):
    return 0 == 500000 - 1000*a - 1000*b + a*b

def getC(a,b):
    return 1000-a-b

for i in range(500):
    for j in range(500):
        if(checkFormula(i,j)):
            c = getC(i,j)
            if(checkABC(i,j,c)):
                print(i,j,c)
                solution = i*j*c
                
print(solution)