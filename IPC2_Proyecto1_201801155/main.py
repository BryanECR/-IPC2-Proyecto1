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
            Curso: IPC2
            Correo electronico: caal320@gmail.com
        '''
        print(opciones)
        op = int(input("Ingrese la Opcion que desea por teclado: "))
        if(op == 1):
            print("elegiste la opcion 1")
        elif(op == 2):
            print("Escogiste la Opcion 2")
        elif(op == 3):
            print("Escogiste la Opcion 2")
        elif(op == 4):
            print(datos)
        elif(op == 5):
            print("Escogiste la Opcion 2")
        elif(op == 6):
            break


menu()