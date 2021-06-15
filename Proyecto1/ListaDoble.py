from ListaSimple import *
import XML


class nodoMatriz:
    def __init__(self, matriz=None, n=0, m=0, next=None):
        self.matriz = matriz
        self.n = n
        self.next = next
        self.m = m


class linked_list_circular:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertar(self, matriz, n, m):
        if self.size == 0:
            self.head = nodoMatriz(matriz=matriz, n=n, m=m)
            self.head.next = self.head
        else:
            nodo = self.head
            while nodo.next is not self.head:
                nodo = nodo.next
            new_node = nodoMatriz(matriz=matriz, n=n, m=m, next=self.head)
            nodo.next = new_node
        self.size += 1

    def comprobar_Nombre(self, nombre):
        nodo = self.head
        # existe = False
        if self.size == 0:
            return True
        else:
            while nodo.next is not self.head:
                # if nodo.nombre is nombre:
                if nodo.matriz.nombre is nombre:
                    return False
                else:
                    nodo = nodo.next
            return True

    def obtener_Nombre(self, indice):
        nodo = self.head
        # existe = False
        if self.size == 0:
            print("matriz vacia")
            return "vacio"
        else:
            for i in range(1, indice):
                nodo = nodo.next
            return nodo.matriz.nombre
            # return nodo.nombre

    def obtener_Nombres(self):
        nombres = []
        nodo = self.head
        if self.size == 0:
            print("matriz vacia")
            return None
        else:
            for i in range(self.size):
                # nombres.append(nodo.nombre)
                nombres.append(nodo.matriz.nombre)
                nodo = nodo.next
            return nombres

    def obtener_Matriz(self, nombre):
        nodo = self.head
        if self.size == 0:
            return None
        else:
            for i in range(self.size):
                if nodo.matriz.nombre == nombre:
                    return nodo.matriz
                else:
                    nodo = nodo.next
            return None

    def reemplazar_Matriz(self, nombre, matriz):
        nodo = self.head
        for i in range(self.size):
            if nodo.matriz.nombre == nombre:
                nodo.matriz = matriz
            else:
                nodo = nodo.next

    def imprimir(self):
        if self.head is None:
            return
        nodo = self.head
        print(f"matriz: {nodo.matriz.nombre} "
              f"| n: {nodo.n} | m: {nodo.m} "
              f"| Espacios llenos: {nodo.matriz.espaciosLlenos} "
              f"| Espacios Vacios: {nodo.matriz.espaciosVacios}")
        print(nodo.matriz.imprimir())
        while nodo.next is not self.head:
            nodo = nodo.next
            print(f"matriz: {nodo.matriz.nombre} "
                  f"| n: {nodo.n} | m: {nodo.m} "
                  f"| Espacios llenos: {nodo.matriz.espaciosLlenos} "
                  f"| Espacios Vacios: {nodo.matriz.espaciosVacios}")
            print(nodo.matriz.imprimir())

    def imprimirNombres(self):
        if self.head is None:
            return
        nodo = self.head
        i = 1
        print(f"{i}: matriz: {nodo.nombre} "
              f"| n: {nodo.n} | m: {nodo.m} "
              f"| Espacios llenos: {nodo.matriz.espaciosLlenos} "
              f"| Espacios Vacios: {nodo.matriz.espaciosVacios}")
        while nodo.next is not self.head:
            nodo = nodo.next
            i += 1
            print(f"{i}: matriz: {nodo.nombre} "
                  f"| n: {nodo.n} | m: {nodo.m} "
                  f"| Espacios llenos: {nodo.matriz.espaciosLlenos} "
                  f"| Espacios Vacios: {nodo.matriz.espaciosVacios}")