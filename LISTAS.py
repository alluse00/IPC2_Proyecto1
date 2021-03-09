
class nodoNumero:
    def __init__(self, numero=None, y=None, next=None):
        self.numero=numero
        self.next=next
        self.y=y

def __init__(self):
    self.head=None

def insertar(self, fila):
    if not self.head:
        self.head = nodoFila(fila=fila)
        return
    current=self.head
    while current.next:
        current.current.next
    current.next = nodoFila(fila=fila)

def insertarPosicion(self, x, y, numero):
    nodo=self.head
    while nodo.next is not self.head:
        if nodo.fila.x ==x :
        nodo.fila.insertarPosicion(numero, y)
        break
    else:
        nodo=nodo.next

def comprobarPosicion(self, x, y):
    nodo=self.head
    while nodo.next is not self.head:
        if nodo.fila.x ==x:
            return nodo.fila.comprobarPosicion(y)
        else:
            nodo=nodo.next

def imprimir(self):
    nodo=self.head
    while nodo is not None:
        print(nodo.fila.imprimir())
        nodo=nodo.next

def reducirMatriz(self):
    actual = self.head
    while actual is not None:
        siguiente = self.head.next
        while siguiente is not None:
            if actual.fila.obtenerBinario()==siguiente.fila.obtenerBinario():
                self.sumarFila(actual.fila, siguiente.fila)
                actual.fila.frecuencia += 1
                filaAeliminar = siguiente.fila.x
                siguiente = actual.next
                self.eliminarfila(filaAeliminar)
            else:
                siguiente=siguiente
        actual=actual.next

def sumarFila(self, fila1, fila2):
    actualFila1 = fila1.head
    actualFila2 = fila2.head
    while actualFila1 is not None: