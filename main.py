from Funciones.lectura import Lectura
from lista.Lista import ListaCircular
from Funciones.Grafica import Graficar
from Funciones.MSalida import ArchivoDeSalida

listaC = ListaCircular()
graficar = Graficar()

def leer_Archivo_E_Ingresarlo_en_la_lista(ruta):
    
    data = Lectura.datos(ruta)

    for i in range(len(data)):
        nombre = data[i].get('Nombre')
        filas = data[i].get('filas')
        columnas = data[i].get('columnas')
        matriz = data[i].get('matriz')
        listaC.incertar(nombre,filas,columnas,matriz)

#IMPRIMIR LA LISTA ENLAZADA


#ELEGIR LA MATRIZ SE QUIERE GRAFICAR
def matriz_A_Graficar(nombre):
    matrix = listaC.buscar(nombre)
    filas = len(matrix)
    columnas = len(matrix[0])

    cadena = Graficar.generarContenido(nombre,filas,columnas,matrix)

    Graficar.generarGrafica(cadena)


def menu():
    while(True):
        opciones = '''
        ***************** Menu **********************
        *       1. Cargar Archivo                   *
        *       2. Procesar Archivo                 *
        *       3. Escribir Archivo de salida       *
        *       4. Mostrar Datos del Estudiante     *
        *       5. Generar Grafica de una matriz    *
        *       6. Generar Grafica de Lista         *
        *       7. Salir                            *
        *********************************************
        '''
        datos = ''' 
            Nombre: Bryan Eduardo Caal Racanac
            Carnet: 201801155
            Curso: Introduccion a la Programacion y Computacion 2
            Seccion: D
            4to Semestre
            Correo electronico: caal320@gmail.com
        '''
        print(opciones)
        op = int(input("Ingrese la Opcion que desea por teclado: "))
        if(op == 1):
            ruta = str(input("Ingrese la ruta del archivo que desee leer: "))
            leer_Archivo_E_Ingresarlo_en_la_lista(ruta)
        elif(op == 2):
            print("Escogiste la Opcion 2")
        elif(op == 3):
            print("Escogiste la Opcion 3")
            
        elif(op == 4):
            print(datos)
        elif(op == 5):
            listaC.recorrer()
            search = input("Ingrese el nombre de la matriz que desea Graficar: ")
            matriz_A_Graficar(search)
        elif(op == 6):
            print("Graficar la lista circular")
        elif(op == 7):
            break
        else:
            print("Opcion No valida....")
            print("Ingresar un Numero del 1 al 7 por el teclado numerico")


menu()