import os

def GraficarMatriz(nombre,filas,columnas,matriz):
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

def generarGrafica(cadena):
    file = open("graficaMatriz.dot","w")
    file.write("digraph G {\n"+cadena+"\n}")
    file.close()
    os.system('dot -Tpng graficaMatriz.dot -o graficaMatriz.png')


cadena = GraficarMatriz(Nombre,filas,columnas,matriz_2)
generarGrafica(cadena)
