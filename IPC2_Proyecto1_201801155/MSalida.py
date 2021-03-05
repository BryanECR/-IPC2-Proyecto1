

class ArchivoDeSalida:

    def salida(matrix):
        cadena = ''
        cadena += "<?xml version='1.0'?>\n<matrices nombre='Salida' n='"+str(len(matrix))+"' m='"+str(len(matrix[0]))+"'>\n    <matriz>\n"

        for f in range(len(matrix)):
            for c in range(len(matrix[0])):
                cadena += '        <dato x ="'+str(f)+'" y ="'+str(c)+'">'+str(matrix[f][c])+'</dato>\n'

        cadena += "    </matriz>\n</matrices>"

        
        file = open("Salida.xml","w")
        file.write(cadena)
        file.close()

    print(salida(matrizPrueba))
