matriz_1 = [[5,0,6,0],[2,0,0,4],[8,0,6,0],[3,0,0,1]]
matriz_2 = [[4,2,0,1,5,0],[0,4,0,8,2,6],[7,9,0,1,5,0],[0,4,0,8,2,6],[4,2,3,5,9,4],[5,3,0,1,5,0],[1,0,5,8,6,3]]
matriz_3 = [[8,0,8,0,8,0],[0,5,0,6,0,8],[8,9,4,5,6,1],[1,0,1,0,1,0]]

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
def crearMatrixFinal(fila1,fila2,matrizNormal):
    matrizFinal = []
    print(fila1, fila2)
    for i in range(len(matrizNormal)):
        if(i == fila1):
            matrizFinal.append(sumar(matrizNormal,fila1,fila2,len(matrizNormal[0])))
        elif(i == fila2):
            continue
        else:
            continue
    
    return matrizFinal


#COMPARAR MATRICES, SUMAR Y CREAR MATRIZ RESULTANTE
def comparar(filas,matrixBin,matrizNormal):
    matrizFinal = 0
    contador = 0
    frecuencia = len(matrixBin)
    while(contador < filas):
        contador_2 = contador + 1
        while(contador_2 < filas):
            if(matrixBin[contador] == matrixBin[contador_2]):
                matrizFinal = crearMatrixFinal(contador,contador_2,matrizNormal)
                frecuencia = frecuencia - 2
                
            contador_2 = contador_2 + 1
    
        contador = contador + 1

    return matrizFinal

#CREAR MATRIZ BINARIA A PARTIR DE UNA MATRIZ NORMAL
def normalABin(matriz):
    matrizVacia = []
    filas = len(matriz)
    columnas = len(matriz[0])
    matrix = createBin(filas,columnas,matrizVacia)
    matrixNewbBin = convertBin(filas,columnas,matriz,matrix)

    return matrixNewbBin

#DESVERGUE DESVERGUE
def start(MatrizNo):
    matrizBin = normalABin(matriz_3)
    resultado = comparar(len(matriz_3),matrizBin,MatrizNo)

    return resultado

print(start(matriz_2))