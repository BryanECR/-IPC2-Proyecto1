class Procesar():

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
        matrix = Procesar.createBin(filas,columnas,matrizVacia)
        matrixNewbBin = Procesar.convertBin(filas,columnas,matriz,matrix)

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
                matrizFinal.append(Procesar.sumar(matrizNormal,fila1,fila2,len(matrizNormal[0])))
            elif(i == fila2):
                continue
            else:
                matrizFinal.append(matrizNormal[i])
        
        return matrizFinal

    #IDENTIFICA LAS FILAS IGUALES Y RETORNA UNA MATRIZ NUEVA CON LAS FILAS SUMADAS
    def identificar(pivote,filas,matrixBin,matrixNormal):
        contador = pivote +1 
        matrix = 0
        while(contador < filas):
            if(matrixBin[pivote] == matrixBin[contador]):
                matrix = Procesar.crearMatrixRecursiva(pivote,contador,matrixNormal)
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
            

    #START
    def startConWhile(matrixNormal):
        pivote = 0
        matrixNueva = matrixNormal
        while(True):
            #print(pivote)
            #print(len(matrixNueva))
            if(pivote == len(matrixNueva)-1 ):
                return matrixNueva
                break

            elif(Procesar.comparar2(pivote,Procesar.normalABin(matrixNueva)) == True):
                nuevaMatrix = Procesar.identificar(pivote,len(Procesar.normalABin(matrixNueva)),Procesar.normalABin(matrixNueva),matrixNueva)
                # print(nuevaMatrix)
                matrixNueva = nuevaMatrix
            
            else:
                pivote = pivote +1
