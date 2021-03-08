import os

class Graficar:

    def __init__(self):
        pass

    #RECIBE LA MATRIZ A GRAFICAR Y LA CONVIERTE EN UNA CADENA DE TEXTO
    def generarContenido(nombre,filas,columnas,matriz):
        cadena = ""
        cadena += 'Nombre[label="'+nombre+'"]\n'
        cadena += 'Filas[label= "n='+str(filas)+'"]\n'
        cadena += 'Columnas[label= "m='+str(columnas)+'"]\n'
        
        for f in range(len(matriz)):
            for c in range(len(matriz[0])):
                cadena += "Nodo"+str(f)+str(c)+'[label="'+str(matriz[f][c])+'"]\n'

        cadena += "Nombre -> Filas\n"
        cadena += "Nombre -> Columnas\n"

        fila = 0
        
        while(fila < len(matriz)):
            columna = 0
            cadena += "Nombre -> Nodo"+str(fila)+str(columna)+"\n"
            while(columna < len(matriz[0])-1):
                cadena += "Nodo"+str(fila)+str(columna)+" -> Nodo"+str(fila)+str(columna+1)+"\n"
                columna = columna +1
            fila = fila+1

        return cadena

    #GENERA EL ARCHIVO DOT Y LO CONVIERTE A PNG
    def generarGrafica(cadena):
        file = open("graficaMatriz.dot","w")
        file.write("digraph G {\n"+cadena+"\n}")
        file.close()
        print("************** La Grafica se realizo con exito **************")
        os.system('dot -Tpng graficaMatriz.dot -o graficaMatriz.png')

