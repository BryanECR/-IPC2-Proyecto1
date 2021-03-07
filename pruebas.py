matriz_2 = [[4,2,0,1,5,0],[0,4,0,8,2,6],[7,9,0,1,5,0],[0,4,0,8,2,6],[4,2,3,5,9,4],[5,3,0,1,5,0],[1,0,5,8,6,3]]
matrizBinaria = [[1,1,0,1,1,0],[0,1,0,1,1,1],[1,1,0,1,1,0],[0,1,0,1,1,1],[1,1,1,1,1,1],[1,1,0,1,1,0],[1,0,1,1,1,1]]


#CONVERTIR A BIDIMENCIONAL A BINARIA
def convertBin(filas,columnas,matrixOld,matrixNew):
    for f in range(filas):
        for c in range(columnas):
            if(matrixOld[f][c] == 0):
                matrixNew[f][c] = 0
            else:
                matrixNew[f][c] = 1

    return matrixNew

#CREAR LA MATRIZ BIDIMENSIONAL
def createBin(filas,columnas,mat):
    for i in range(filas):
        mat.append([0]*columnas)

    return mat

#CREAR MATRIZ BINARIA A PARTIR DE UNA MATRIZ NORMAL
def normalABin(matriz):
    matrizVacia = []
    filas = len(matriz)
    columnas = len(matriz[0])
    matrix = createBin(filas,columnas,matrizVacia)
    matrixNewbBin = convertBin(filas,columnas,matriz,matrix)

    return matrixNewbBin

#SUMAR FILAS
def sumar(matrixNormal,fila1,fila2,columnas):
    arrayResultante = []
    for c in range(columnas):
        num1 = matrixNormal[fila1][c]
        num2 = matrixNormal[fila2][c]
        resultado = num1 + num2
        arrayResultante.append(resultado)

    return arrayResultante

#CREAR MATRIZ FINAL
def crearMatrixRecursiva(fila1,fila2,matrizNormal):
    matrizFinal = []
    for i in range(len(matrizNormal)):
        if(i == fila1):
            matrizFinal.append(sumar(matrizNormal,fila1,fila2,len(matrizNormal[0])))
        elif(i == fila2):
            continue
        else:
            matrizFinal.append(matrizNormal[i])
    
    return matrizFinal

#COMPARAR FILAS DE LA MATRIZ BINARIA
def comparar(filas,matrixBin):
    iguales = False
    contador = 0
    while(contador < filas):
        contador_2 = contador + 1
        while(contador_2 < filas):
            if(matrixBin[contador] == matrixBin[contador_2]):
                iguales = True
                
            contador_2 = contador_2 + 1
    
        contador = contador + 1

    return iguales


def identificar(pivote,filas,matrixBin,matrixNormal):
    contador = pivote +1 
    matrix = 0
    while(contador < filas):
        if(matrixBin[pivote] == matrixBin[contador]):
            matrix = crearMatrixRecursiva(pivote,contador,matrixNormal)
            break
        contador = contador +1

    return matrix

#ENCUENTRA DOS LINEAS IGUALES  
def comparar2(pivote,matrixBin):
    iguales = False
    contador = pivote+1
    while(contador < len(matrixBin)):
        if(matrixBin[pivote] == matrixBin[contador]):
            iguales = True
            break

        contador = contador +1
    
    return iguales
               

def start(pivote,matrixNormal):
    nuevaMatrix = 0
    Binaria = normalABin(matrixNormal)
    if(comparar2(pivote,Binaria) == True):
        nuevaMatrix = identificar(pivote,len(Binaria),Binaria,matrixNormal)
    
    return nuevaMatrix

print(start(0,matriz_2))

    





"""
print('Matriz original')
print(matriz_2)
print('convertir la matriz original a 0 y 1')
Binaria = normalABin(matriz_2)
print(Binaria)
print('tomando la fila 0 como pivote identificar si existe una fila identica')
print(comparar2(0,Binaria))
print('sumar las primeras dos filas iguales y crear una nueva matriz a partir del resultado')
nuevaMatrix = identificar(0,len(Binaria),Binaria,matriz_2)
print(nuevaMatrix)
#*************************************************************************************************
print('pasar la nueva matriz a 0 y 1')
Binaria = normalABin(nuevaMatrix)
print(Binaria)
print('tomando la fila 0 como pivote identificar si existe una fila identica')
print(comparar2(0,Binaria))
print('sumar las primeras dos filas iguales y crear una nueva matriz a partir del resultado')
nuevaMatrix = identificar(0,len(Binaria),Binaria,nuevaMatrix)
print(nuevaMatrix)
#*************************************************************************************
print('pasar la nueva matriz a 0 y 1')
Binaria = normalABin(nuevaMatrix)
print(Binaria)
print('tomando la fila 0 como pivote identificar si existe una fila identica')
print(comparar2(0,Binaria))
print('Como ya no existen filas iguales a la 0 el pivote se cambia a 1 y se repite el proceso')
#************************************************************************************
print('Se compara si existe otra fila identica a la fila 1')
print(comparar2(1,Binaria))
print('sumar las primeras dos filas iguales y crear una nueva matriz a partir del resultado')
nuevaMatrix = identificar(1,len(Binaria),Binaria,nuevaMatrix)
print(nuevaMatrix)
#***********************************************************************************
print('se pasa la nueva matriz a 0 y 1 y se compara si existe otra fila igual')
Binaria = normalABin(nuevaMatrix)
print(comparar2(1,Binaria))
#********************************************************
print('Como ya no existen filas iguales a la 0 el pivote se cambia a 2 y se repite el proceso')
print('Se pasa a 1 y 0 y compara si existe otra fila identica a la fila 2')
print(comparar2(2,Binaria))
print('como ya no existen filas identicas el resultado seria')
print(nuevaMatrix)
"""