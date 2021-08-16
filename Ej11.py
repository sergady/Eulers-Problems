# Carga de la matriz en la variable "matriz"
# ----------------------------------------------------------------------------------------------------------------------------
fichero = open("matriz.txt")
matrizFichero = fichero.readlines()
matriz = []
for i in range(len(matrizFichero)):
    matriz.append(matrizFichero[i].split())

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(matriz[i][j]) 

# ----------------------------------------------------------------------------------------------------------------------------

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
def productDown(matrix, i, j):
    if(i+4 >= len(matrix)):
        return 0
    product = 1
    for z in range(i, i+4):
        product *= matrix[z][j]
    return product

def productRight(matrix, i, j):
    if(j+4 >= len(matrix)):
        return 0
    product = 1
    for z in range(j, j+4):
        product *= matrix[i][z]
    return product

def productDiagonallyNatural(matrix, i, j):
    if(i+3 >= len(matrix) or j+3 >= len(matrix)):
        return 0
    product = 1
    for z in range(4):
        product *= matrix[i+z][j+z]
    return product

def productDiagonallyReverse(matrix, i, j):
    if(i-3 < 0 or j+3 >= len(matrix)):
        return 0
    product = 1
    for z in range(4):
        product *= matrix[i-z][j+z]
    return product

def calculateProductsMax(matrix, i, j):
    return max(productDown(matrix,i,j),productRight(matrix,i,j),productDiagonallyNatural(matrix,i,j), productDiagonallyReverse(matrix, i, j))


maxMult = 0 
for i in range(20):
    for j in range(20):
        result = calculateProductsMax(matriz,i,j)
        if(result>maxMult):
            coordinates = (i,j)
            maxMult = result

print(maxMult)
print(coordinates)