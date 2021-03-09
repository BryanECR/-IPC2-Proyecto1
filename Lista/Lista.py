from lista.Nodo import Nodo

class ListaCircular():

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def incertar(self,nombre,fila,columna,matriz):
        if self.vacia():
            self.primero = self.ultimo = Nodo(nombre,fila,columna,matriz)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(nombre,fila,columna,matriz)
            self.ultimo.siguiente  = self.primero 

    def recorrer(self):
        aux = self.primero
        while aux.siguiente != self.primero:
            print(aux.nombre)
            aux = aux.siguiente
        print(aux.nombre)

    def recorrer_Para_Graficar(self):
        nombres = []
        aux = self.primero
        while aux.siguiente != self.primero:
            nombres.append(aux.nombre) 
            aux = aux.siguiente
        nombres.append(aux.nombre)

        return nombres 

    def recorrer_para_salida(self):
        matrixes = []
        aux = self.primero
        while aux.siguiente != self.primero:
            matrixes.append(aux.matriz) 
            aux = aux.siguiente
        matrixes.append(aux.matriz)

        return matrixes 

    def buscar(self,buscar):
        aux = self.primero
        if self.vacia():
            print("No hay elementos en la lista")
        else:
            while aux.siguiente != self.primero:
                
                if aux.nombre == buscar:
                    return aux.matriz
                    break 

                aux = aux.siguiente