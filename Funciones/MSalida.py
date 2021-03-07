class ArchivoDeSalida:

    def salida(matrix):
        cadena = ''
        cadena += "    <matriz nombre='Salida' n='"+str(len(matrix))+"' m='"+str(len(matrix[0]))+"'>\n"

        for f in range(len(matrix)):
            for c in range(len(matrix[0])):
                cadena += '        <dato x ="'+str(f)+'" y ="'+str(c)+'">'+str(matrix[f][c])+'</dato>\n'

        cadena += "    </matriz>\n"

        return cadena

    def generarSalida(cadena):
        arriba = "<?xml version='1.0'?>\n<matrices>\n"
        abajo = "<matrices>\n"
        file = open("Salida.xml","w")
        file.write(arriba+str(cadena)+abajo)
        file.close()

        print("********************************* Grafica Generada Con Exito **********************************************")
