from xml.dom import minidom
from ListaC import *
from ListaS import *

def leerArchivo(ruta):
    doc = minidom.parse(ruta)
    item = doc.getElementsByTagName('matriz')
    matrices = linked_list_circular()
    for elemento in items:
        matrizC = True
        nombre = elemento.attributes['nombre'].value
        n=int(elemento.attributes['n'].value)
        m=int(elemento.attributes['m'].value)
        datos = elemento.getElementsByTagName('dato')
        if matrices.comprobar_Nombre(nombre):
            matriz=crear_matriz(n,m)
            for dato in datos:
                x=int(dato.attributes['x'].value)
                y=int(dato.attributes['y'].value)
                if 0 < x <= n and 0 < y <= m:
                    if not matriz.comprobarPosicion(x,y):
                        matriz.insertarPosicion(x,y,dato.firstChild.data)
                    else:
                        print("posicion repetida")
                        matrizC = False
                else:
                    print("Dato con posiciones fuera de rango")
                    matrizC=False
            if matrizC:
                matrices.insertar(matriz=matriz,nombre=nombre,n=n,m=m)
            else:
                print("Matriz {nombre} no ingresada verifique los datos)
        else:
            print("Matriz {nombre} con nombre repetido")
    return matrices

