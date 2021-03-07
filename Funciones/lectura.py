import xml.etree.ElementTree as ET
tree = ET.parse('lectura.xml')
root = tree.getroot()

class Lectura:
    #INFORMACION DE LA ETIQUETA PADRE
    def father(numero,nombre,filas,columnas):
        print('Numero de matriz: '+str(numero))
        print('Nombre de la matriz: '+nombre)
        print('filas: '+filas)
        print('Columnas: '+columnas)

    #CREATE MATRIZ
    def create(filas,columnas,mat):
        for i in range(filas):
            mat.append([0]*columnas)
        
        return mat


    #RECORRIDO DE LA MATRIZ
    def recorrer():
        name = ''
        rows = ''
        column = ''
        x = ''
        y = ''
        content = ''
        matriz = 0
        for elem in root:
            matrix = []
            name = elem.attrib['name']
            rows = elem.attrib['n']
            column = elem.attrib['m']
            matriz = matriz+1
            father(matriz,name,rows,column)
            create(int(rows),int(column),matrix)
            for subelem in elem:
                x = subelem.attrib['x']
                y = subelem.attrib['y']
                content = subelem.text
                #cont(x,y,content)
                matrix[int(x)-1][int(y)-1] = content
            print('Contenido de la matriz')
            print(matrix)   
            print('**********************************')
        

