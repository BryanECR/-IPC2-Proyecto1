class Nodo():
    def __init__(self,nombre,fila,columna,matriz):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.matriz = matriz
        self.siguiente = None