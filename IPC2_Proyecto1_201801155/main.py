from MSalida import ArchivoDeSalida
from Grafica import Graficar

matrizPrueba = [[1,0,5,12,3,7,9],[0,0,0,1,5,4,8],[1,1,1,1,1,1,0],[2,0,0,0,0,0,2]]

def menu():
    while(True):
        opciones = '''
        ***************** Menu *******************
        *       1. Cargar Archivo                *
        *       2. Procesar Archivo              *
        *       3. Escribir Archivo de salida    *
        *       4. Mostrar Datos del Estudiante  *
        *       5. Generar Grafica               *
        *       6. Salir                         *
        ******************************************
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
            print("elegiste la opcion 1")
        elif(op == 2):
            print("Escogiste la Opcion 2")
        elif(op == 3):
            print("Escogiste la Opcion 3")
            ArchivoDeSalida.salida(matrizPrueba)
        elif(op == 4):
            print(datos)
        elif(op == 5):
            print("Escogiste la Opcion 2")
        elif(op == 6):
            break
        else:
            print("Opcion No valida....")
            print("Ingresar un Numero del 1 al 6 por el teclado numerico")


menu()