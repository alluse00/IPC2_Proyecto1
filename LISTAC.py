class nodoNumero:
    def __init__(self, numero=None,y=None,next=None):
        self.numero=numero
        self.next=next
        self.y=y

class Fila:

    def __init__(self, x=None, frecuencia=None):
        self.head = None
        self.x=x
        self.frecuencia=frecuencia
    
    def insertar(self, numero, y):
        if not self.head:
            self.head=nodoNumero(numero=numero, y=y)
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=nodoNumero(numero=numero, y=y)

    def insertarPosicion(self, numero, y):
        current=self.head
        while current.next is not self.head:
            if current.y ==y:
                current.numero=numero
                break
            else:
                current=current.next
                
    def comprobarPosicion(self, y):
        current=self.head
        while current.next is not self.head:
            if current.y==y:
                if current.numero is not None:
                    return True
                else:
                    return False
            else:
                print("Nose que sea esto")