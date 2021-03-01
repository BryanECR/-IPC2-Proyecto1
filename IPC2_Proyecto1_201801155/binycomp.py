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
            print(contador,contador_2)
            if(matrixBin[contador] == matrixBin[contador_2]):
                print('iguales'+str(contador)+" Y "+str(contador_2))
                iguales = True
                
            contador_2 = contador_2 + 1
    
        contador = contador + 1

    return iguales


def identificar(pivote,filas,matrixBin,matrixNormal):
    contador = pivote +1 
    matrix = 0
    while(contador < filas):
        if(matrixBin[pivote] == matrixBin[contador]):
            print(pivote,contador)
            matrix = crearMatrixRecursiva(pivote,contador,matrixNormal)
            break
        contador = contador +1

    return matrix

#ENCUENTRA DOS LINEAS IGUALES  
def comparar2(matrixBin):
    iguales = False
    for pivote in range(len(matrixBin)):
        linea = pivote +1 
        while(linea < len(matrixBin)):
            if(matrixBin[pivote] == matrixBin[linea]):
                iguales = True
                break
            linea = linea + 1
    
    return iguales





print(comparar2(matrizBinaria))

'''

primeraUtil = algo(0,1,matrizBinaria,matriz_2)
print(primeraUtil)
print('convertimos esa matriz a binaria')
primeraBin = algo(0,1,matrizBinaria,matriz_2)
print(normalABin(primeraBin))
print('valuamos esa nueva matriz binaria para ver si tiene filas iguales')
print(comparar(len(primeraBin),primeraBin))
print('Las identificamos, las sumamos y retornamos la nueva matriz')
segundaUtil = algo(0,1,primeraBin,primeraUtil)
print(segundaUtil)
print('Volvemos a convertirla en binaria')
segundaBin = algo(0,1,primeraBin,primeraUtil)
print(normalABin(segundaBin))
print('verificamos si tiene filas parecidas')
print(comparar(len(segundaBin),segundaBin))
print('Sumamos las filas parecidas y la convertimos a normal otra vez')
terceraUtil = algo(1,2,segundaBin,segundaUtil)
print(terceraUtil)
print('la convertimos a binaria')
terceraBinaria = normalABin(terceraUtil)
print(terceraBinaria)
print('verificamos si tiene filas parecidas')
print(comparar(len(terceraBinaria),terceraBinaria))

'''