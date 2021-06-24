from nodo import NodoMatriz
import os

def crear(id, name, shape):
    return id + "[label=\"" + name + "\",shape=" + shape + "]\n"

def unir(nodo1, nodo2):
    return nodo1 + "->" + nodo2 + "\n"

class Matriz():
    def __init__(self):
        self.raiz = NodoMatriz(-1, -1, "Raiz")

    def findX(self, x):
        temp = self.raiz
        while temp is not None:
            if (temp.x == x):
                return temp
            temp = temp.siguiente
        return None

    def findY(self, y):
        temp = self.raiz
        while temp is not None:
            if (temp.y == y):
                return temp
            temp = temp.abajo
        return None

    def agregarColumna(self, nuevo, cabezaColumna):
        temp = cabezaColumna
        flag = False
        while True:
            if (temp.x == nuevo.x):
                temp.y = nuevo.y
                temp.color = nuevo.color
                return temp
            elif (temp.x > nuevo.x):
                flag = True
                break
            if (temp.siguiente is not None):
                temp = temp.siguiente
            else:
                break
        if flag:
            nuevo.siguiente = temp
            temp.anterior.siguiente = nuevo
            nuevo.anterior = temp.anterior
            temp.anterior = nuevo
        else:
            temp.siguiente = nuevo
            nuevo.anterior = temp
        return nuevo

    def crearColumna(self, x):
        cabezaColumna = self.raiz
        columna = self.agregarColumna(NodoMatriz(x, -1, ("X=" + str(x))), cabezaColumna)
        return columna

    def agregarFila(self, nuevo, cabezaFila):
        temp = cabezaFila
        flag = False
        while True:
            if (temp.y == nuevo.y):
                temp.x = nuevo.x
                temp.color = nuevo.color
            elif (temp.y > nuevo.y):
                flag = True
                break
            if (temp.abajo is not None):
                temp = temp.abajo
            else:
                break
        if flag:
            nuevo.abajo = temp
            temp.arriba.abajo = nuevo
            nuevo.arriba = temp.arriba
            temp.arriba = nuevo
        else:
            temp.abajo = nuevo
            nuevo.arriba = temp
        return nuevo

    def crearFila(self, y):
        cabezaFila = self.raiz
        fila = self.agregarFila(NodoMatriz(-1, y, ("Y=" + str(y))), cabezaFila)
        return fila

    def insertarElemento(self, x, y, color):
        nuevo = NodoMatriz(x, y, color)
        nodoColumna = self.findX(x)
        nodoFila = self.findY(y)
        if (nodoColumna is None and nodoFila is None):
            nodoColumna = self.crearColumna(x)
            nodoFila = self.crearFila(y)
            nuevo = self.agregarColumna(nuevo, nodoFila)
            nuevo = self.agregarFila(nuevo, nodoColumna)
        elif (nodoColumna is None and nodoFila is not None):
            nodoColumna = self.crearColumna(x)
            nuevo = self.agregarColumna(nuevo, nodoFila)
            nuevo = self.agregarFila(nuevo, nodoColumna)
        elif (nodoColumna is not None and nodoFila is None):
            nodoFila = self.crearFila(y)
            nuevo = self.agregarColumna(nuevo, nodoFila)
            nuevo = self.agregarFila(nuevo, nodoColumna)
        elif (nodoColumna is not None and nodoFila is not None):
            nuevo = self.agregarColumna(nuevo, nodoFila)
            nuevo = self.agregarFila(nuevo, nodoColumna)

