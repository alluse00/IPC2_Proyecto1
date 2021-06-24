from tkinter import *
from matrizDispersa import Matriz
import random
from tkinter import messagebox as MessageBox

matriz=Matriz()
colorJ1 = ""
colorJ2 = ""
valorY=""
valorX=""
matrizBotones=[]
listaBotones=[]
piezaRandom=0

def Dim():
    global valorX, valorY
    valorX=dimX.get()
    valorY=dimY.get()
    fil = 1/int(valorY)
    col= 1/int(valorX)
    for y in range(int(valorX)):
        matrizBotones.append([])
        for x in range(int(valorY)):
            matrizBotones[y].append(Button(frameTablero))
            matrizBotones[y][x].config(bg="white", borderwidth=2, relief="solid")
            matrizBotones[y][x].place(relx=col*y, rely=fil*x, relwidth=col, relheigh=fil)
    for y in range(int(valorY)):
        listaBotones.append([])
        for x in range(int(valorX)):
            listaBotones[y].append([x,y,True,"SinColor"])

def defayuda():
    MessageBox.showinfo("AYUDA","Programador: Allan Josué Rafael Morales\n IPC 2 - Curso de vacaciones Junio 2021")

def color1(boton):
    global colorJ1, botonRojo2
    if boton == 1:
        colorJ1='red'
        print(colorJ1)
    if boton == 2:
        colorJ1 = 'blue'
        print(colorJ1)
    if boton == 3:
        colorJ1 = 'yellow'
        print(colorJ1)
    if boton == 4:
        colorJ1 = 'green'
        print(colorJ1)

def color2(boton):
    global colorJ2
    if boton == 1:
        if colorJ1 == 'red':
            MessageBox.showinfo("Error","Ya han elegido el color rojo")
        else:
            colorJ2='red'
            print(colorJ2)
    if boton == 2:
        if colorJ1 == 'blue':
            MessageBox.showinfo("Error","Ya han elegido el color azul")
        else:
            colorJ2='blue'
            print(colorJ2)
            colorJ2 = 'blue'
    if boton == 3:
        if colorJ1 == 'yellow':
            MessageBox.showinfo("Error","Ya han elegido el color amarillo")
        else:
            colorJ2='yellow'
            print(colorJ2)
            colorJ2 = 'yellow'
    if boton == 4:
        if colorJ1 == 'green':
            MessageBox.showinfo("Error","Ya han elegido el color verde")
        else:
            colorJ2='green'
            print(colorJ2)
            colorJ2 = 'green'

def randomPieza():
    global piezaRandom
    piezaRandom=random.randint(1,6)

def pintarJ1():
    global valorX, valorY, colorJ1, piezaRandom
    colorBoton = colorJ1
    tamMatriz = len(matrizBotones)
    posX = (int(coorX1.get()) - 1)
    posY = (int(coorY1.get()) - 1)
    flag = True
    if (tamMatriz <= 0):
        MessageBox.showinfo("Error", "Tablero no ha sido creado")
    else:
        # L INVERTIDA
        if (piezaRandom == 1):
            for i in range(4):
                if (listaBotones[posX][posY + i][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                    flag = False
                    if (i == 3):
                        if (listaBotones[posX - 1][posY + i][2] == False):
                            MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                            flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX][posY + i][2] == True):
                        listaBotones[posX][posY + i][2] = False
                        listaBotones[posX][posY + i][3] = colorJ1
                        matrizBotones[posX][posY + i].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1), int(posY + 1 + i), colorJ1)
                        if (i == 3):
                            if (listaBotones[posX - 1][posY + i][2] == True):
                                listaBotones[posX - 1][posY + i][2] = False
                                listaBotones[posX - 1][posY + i][3] = colorJ1
                                matrizBotones[posX - 1][posY + i].config(bg=colorBoton, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX + 1 - 1), int(posY + 1 + i), colorJ1)
        # L NORMAL
        if (piezaRandom == 2):
            for i in range(4):
                if (listaBotones[posX][posY + i][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                    flag = False
                    if (i == 3):
                        if (listaBotones[posX + 1][posY + i][2] == False):
                            MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                            flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX][posY + i][2] == True):
                        listaBotones[posX][posY + i][2] = False
                        listaBotones[posX][posY + i][3] = colorJ1
                        matrizBotones[posX][posY + i].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1), int(posY + 1 + i), colorJ1)
                        if (i == 3):
                            if (listaBotones[posX + 1][posY + i][2] == True):
                                listaBotones[posX + 1][posY + i][2] = False
                                listaBotones[posX + 1][posY + i][3] = colorJ1
                                matrizBotones[posX + 1][posY + i].config(bg=colorBoton, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX + 1 + 1), int(posY + 1 + i), colorJ1)
        # CUADRADO
        if (piezaRandom == 3):
            for i in range(4):
                if (i == 0):
                    if (listaBotones[posX][posY][2] == False):
                        MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                        flag = False
                elif (i == 1):
                    if (listaBotones[posX + 1][posY][2] == False):
                        MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                        flag = False
                elif (i == 2):
                    if (listaBotones[posX][posY + 1][2] == False):
                        MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                        flag = False
                elif (i == 3):
                    if (listaBotones[posX + 1][posY + 1][2] == False):
                        MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                        flag = False
            if (flag == True):
                for i in range(4):
                    if (i == 0):
                        if (listaBotones[posX][posY][2] == True):
                            listaBotones[posX][posY][2] = False
                            listaBotones[posX][posY][3] = colorJ1
                            matrizBotones[posX][posY].config(bg=colorBoton, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX + 1), int(posY + 1), colorJ1)
                    elif (i == 1):
                        if (listaBotones[posX + 1][posY][2] == True):
                            listaBotones[posX + 1][posY][2] = False
                            listaBotones[posX + 1][posY][3] = colorJ1
                            matrizBotones[posX + 1][posY].config(bg=colorBoton, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX + 1 + 1), int(posY + 1), colorJ1)
                    elif (i == 2):
                        if (listaBotones[posX][posY + 1][2] == True):
                            listaBotones[posX][posY + 1][2] = False
                            listaBotones[posX][posY + 1][3] = colorJ1
                            matrizBotones[posX][posY + 1].config(bg=colorBoton, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX + 1), int(posY + 1 + 1), colorJ1)
                    elif (i == 3):
                        if (listaBotones[posX + 1][posY + 1][2] == True):
                            listaBotones[posX + 1][posY + 1][2] = False
                            listaBotones[posX + 1][posY + 1][3] = colorJ1
                            matrizBotones[posX + 1][posY + 1].config(bg=colorBoton, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX + 1 + 1), int(posY + 1 + 1), colorJ1)
        # PIRAMIDE
        if (piezaRandom == 4):
            for i in range(4):
                if (listaBotones[posX + i][posY][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                    flag = False
                    if (i == 1):
                        if (listaBotones[posX + i][posY - 1][2] == False):
                            MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY - 1) + ")")
                            flag = False
                    if (i == 2):
                        if (listaBotones[posX + i][posY - 1][2] == False):
                            MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY - 1) + ")")
                            flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX + i][posY][2] == True):
                        listaBotones[posX + i][posY][2] = False
                        listaBotones[posX + i][posY][3] = colorJ1
                        matrizBotones[posX + i][posY].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1 + i), int(posY + 1), colorJ1)
                        if (i == 1):
                            if (listaBotones[posX + i][posY - 1][2] == True):
                                listaBotones[posX + i][posY - 1][2] = False
                                listaBotones[posX + i][posY - 1][3] = colorJ1
                                matrizBotones[posX + i][posY - 1].config(bg=colorBoton, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX + 1 + i), int(posY + 1 - 1), colorJ1)
                        if (i == 2):
                            if (listaBotones[posX + i][posY - 1][2] == True):
                                listaBotones[posX + i][posY - 1][2] = False
                                listaBotones[posX + i][posY - 1][3] = colorJ1
                                matrizBotones[posX + i][posY - 1].config(bg=colorBoton, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX + 1 + i), int(posY + 1 - 1), colorJ1)
        # LINEA VERTICAL
        if (piezaRandom == 5):
            for i in range(4):
                if (listaBotones[posX][posY + i][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                    flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX][posY + i][2] == True):
                        listaBotones[posX][posY + i][2] = False
                        listaBotones[posX][posY + i][3] = colorJ1
                        matrizBotones[posX][posY + i].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1), int(posY + 1 + i), colorJ1)
        # LINEA HORIZONTAL
        if (piezaRandom == 6):
            for i in range(4):
                if (listaBotones[posX + i][posY][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                    flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX + i][posY][2] == True):
                        listaBotones[posX + i][posY][2] = False
                        listaBotones[posX + i][posY][3] = colorJ1
                        matrizBotones[posX + i][posY].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1 + i), int(posY + 1), colorJ1)
    randomPieza()

def pintarJ2():
    global valorX, valorY, colorJ2, piezaRandom
    colorBoton = colorJ2
    tamMatriz = len(matrizBotones)
    posX = (int(coorX2.get()) - 1)
    posY = (int(coorY2.get()) - 1)
    flag = True
    if (tamMatriz <= 0):
        MessageBox.showinfo("Error", "Tablero no ha sido creado")
    else:
        # L INVERTIDA
        if (piezaRandom == 1):
            for i in range(4):
                if (listaBotones[posX][posY + i][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                    flag = False
                    if (i == 3):
                        if (listaBotones[posX - 1][posY + i][2] == False):
                            MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                            flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX][posY + i][2] == True):
                        listaBotones[posX][posY + i][2] = False
                        listaBotones[posX][posY + i][3] = colorJ2
                        matrizBotones[posX][posY + i].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1), int(posY + 1 + i), colorJ2)
                        if (i == 3):
                            if (listaBotones[posX - 1][posY + i][2] == True):
                                listaBotones[posX - 1][posY + i][2] = False
                                listaBotones[posX - 1][posY + i][3] = colorJ2
                                matrizBotones[posX - 1][posY + i].config(bg=colorBoton, borderwidth=2,relief="solid")
                                matriz.insertarElemento(int(posX + 1 - 1), int(posY + 1 + i), colorJ2)
        # L NORMAL
        if (piezaRandom == 2):
            for i in range(4):
                if (listaBotones[posX][posY + i][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                    flag = False
                    if (i == 3):
                        if (listaBotones[posX + 1][posY + i][2] == False):
                            MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                            flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX][posY + i][2] == True):
                        listaBotones[posX][posY + i][2] = False
                        listaBotones[posX][posY + i][3] = colorJ2
                        matrizBotones[posX][posY + i].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1), int(posY + 1 + i), colorJ2)
                        if (i == 3):
                            if (listaBotones[posX + 1][posY + i][2] == True):
                                listaBotones[posX + 1][posY + i][2] = False
                                listaBotones[posX + 1][posY + i][3] = colorJ2
                                matrizBotones[posX + 1][posY + i].config(bg=colorBoton, borderwidth=2,relief="solid")
                                matriz.insertarElemento(int(posX + 1 + 1), int(posY + 1 + i), colorJ2)
        # CUADRADO
        if (piezaRandom == 3):
            for i in range(4):
                if (i == 0):
                    if (listaBotones[posX][posY][2] == False):
                        MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                        flag = False
                elif (i == 1):
                    if (listaBotones[posX + 1][posY][2] == False):
                        MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                        flag = False
                elif (i == 2):
                    if (listaBotones[posX][posY + 1][2] == False):
                        MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                        flag = False
                elif (i == 3):
                    if (listaBotones[posX + 1][posY + 1][2] == False):
                        MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                        flag = False
            if (flag == True):
                for i in range(4):
                    if (i == 0):
                        if (listaBotones[posX][posY][2] == True):
                            listaBotones[posX][posY][2] = False
                            listaBotones[posX][posY][3] = colorJ2
                            matrizBotones[posX][posY].config(bg=colorBoton, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX + 1), int(posY + 1), colorJ2)
                    elif (i == 1):
                        if (listaBotones[posX + 1][posY][2] == True):
                            listaBotones[posX + 1][posY][2] = False
                            listaBotones[posX + 1][posY][3] = colorJ2
                            matrizBotones[posX + 1][posY].config(bg=colorBoton, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX + 1 + 1), int(posY + 1), colorJ2)
                    elif (i == 2):
                        if (listaBotones[posX][posY + 1][2] == True):
                            listaBotones[posX][posY + 1][2] = False
                            listaBotones[posX][posY + 1][3] = colorJ2
                            matrizBotones[posX][posY + 1].config(bg=colorBoton, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX + 1), int(posY + 1 + 1), colorJ2)
                    elif (i == 3):
                        if (listaBotones[posX + 1][posY + 1][2] == True):
                            listaBotones[posX + 1][posY + 1][2] = False
                            listaBotones[posX + 1][posY + 1][3] = colorJ2
                            matrizBotones[posX + 1][posY + 1].config(bg=colorBoton, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX + 1 + 1), int(posY + 1 + 1), colorJ2)
        # PIRAMIDE
        if (piezaRandom == 4):
            for i in range(4):
                if (listaBotones[posX + i][posY][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                    flag = False
                    if (i == 1):
                        if (listaBotones[posX + i][posY - 1][2] == False):
                            MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY - 1) + ")")
                            flag = False
                    if (i == 2):
                        if (listaBotones[posX + i][posY - 1][2] == False):
                            MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY - 1) + ")")
                            flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX + i][posY][2] == True):
                        listaBotones[posX + i][posY][2] = False
                        listaBotones[posX + i][posY][3] = colorJ2
                        matrizBotones[posX + i][posY].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1 + i), int(posY + 1), colorJ2)
                        if (i == 1):
                            if (listaBotones[posX + i][posY - 1][2] == True):
                                listaBotones[posX + i][posY - 1][2] = False
                                listaBotones[posX + i][posY - 1][3] = colorJ2
                                matrizBotones[posX + i][posY - 1].config(bg=colorBoton, borderwidth=2,relief="solid")
                                matriz.insertarElemento(int(posX + 1 + i), int(posY + 1 - 1), colorJ2)
                        if (i == 2):
                            if (listaBotones[posX + i][posY - 1][2] == True):
                                listaBotones[posX + i][posY - 1][2] = False
                                listaBotones[posX + i][posY - 1][3] = colorJ2
                                matrizBotones[posX + i][posY - 1].config(bg=colorBoton, borderwidth=2,relief="solid")
                                matriz.insertarElemento(int(posX + 1 + i), int(posY + 1 - 1), colorJ2)
        # LINEA HORIZONTAL
        if (piezaRandom == 5):
            for i in range(4):
                if (listaBotones[posX][posY + i][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX) + "," + str(posY + i) + ")")
                    flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX][posY + i][2] == True):
                        listaBotones[posX][posY + i][2] = False
                        listaBotones[posX][posY + i][3] = colorJ2
                        matrizBotones[posX][posY + i].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1), int(posY + 1 + i), colorJ2)
        # LINEA HORIZONTAL
        if (piezaRandom == 6):
            for i in range(4):
                if (listaBotones[posX + i][posY][2] == False):
                    MessageBox.showinfo("Error", "Casilla no valida: (" + str(posX + i) + "," + str(posY) + ")")
                    flag = False
            if (flag == True):
                for i in range(4):
                    if (listaBotones[posX + i][posY][2] == True):
                        listaBotones[posX + i][posY][2] = False
                        listaBotones[posX + i][posY][3] = colorJ2
                        matrizBotones[posX + i][posY].config(bg=colorBoton, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX + 1 + i), int(posY + 1), colorJ2)
    randomPieza()

def botonAceptar():
    global labelJ1,lblX,lblY,botonJ1,labelJ2,coorX1,coorX2,coorY1,coorY2
    ventana.state(newstate='withdraw')
    Dim()
    if lblImagen.place_info() != {}:
        lblImagen.place_forget()

    # SECCION PARA INTRODUCIR LAS PIEZAS J1
    labelJ1 = Label(frameMenu, text="Coordenadas Jugador 1: ", background='darkgray').place(x=60, y=120)
    lblX = Label(frameMenu, text="X: ", background='darkgray').place(x=80, y=150)
    coorX1 = Entry(frameMenu)
    coorX1.place(x=100, y=150, width=20, height=20)
    lblY = Label(frameMenu, text="Y: ", background='darkgray').place(x=130, y=150)
    coorY1 = Entry(frameMenu)
    coorY1.place(x=150, y=150, width=20, height=20)
    botonJ1 = Button(frameMenu, text='Colocar pieza', command=pintarJ1).place(x=85, y=180)

    # SECCION PARA INTRODUCIR LAS PIEZAS J2
    labelJ2 = Label(frameMenu, text="Coordenadas Jugador 2: ", background='darkgray').place(x=60, y=210)
    lblX = Label(frameMenu, text="X: ", background='darkgray').place(x=80, y=240)
    coorX2 = Entry(frameMenu)
    coorX2.place(x=100, y=240, width=20, height=20)
    lblY = Label(frameMenu, text="Y: ", background='darkgray').place(x=130, y=240)
    coorY2 = Entry(frameMenu)
    coorY2.place(x=150, y=240, width=20, height=20)
    botonJ1 = Button(frameMenu, text='Colocar pieza', command=pintarJ2).place(x=85, y=270)


def abrirVentana():
    ventana.state(newstate='normal')

#FUNCIONES PARA ESCOGER EL COLOR
raiz = Tk()
raiz.title("Principal")
raiz.resizable(False, False)
raiz.geometry("1000x600")
raiz.iconbitmap("usacIcono.ico")
raiz.config(bg="Silver")

# VENTANA PARA PEDIR DATOS DE PARTIDA
num = IntVar()
ventana=Toplevel()
ventana.state(newstate='withdraw')
ventana.geometry("300x300")
ventana.resizable(False, False)
ventana.title("Datos de la partida")
lblC1 = Label(ventana, text="Color jugador 1").place(x=110, y=10)
lblC2 = Label(ventana, text="Color jugador 2").place(x=110, y=100)

# JUGADORES ELIGEN EL COLOR Y DIMENSIONES DEL TABLERO
botonRojo1 = Button(ventana, bg="red", width=2, height=2, command = lambda:color1(1)).place(x=105, y=35)
botonAzul1 = Button(ventana, bg="blue", width=2, height=2, command = lambda:color1(2)).place(x=130, y=35)
botonAmarillo1 = Button(ventana, bg="yellow", width=2, height=2, command = lambda:color1(3)).place(x=155, y=35)
botonVerde1 = Button(ventana, bg="green", width=2, height=2, command = lambda:color1(4)).place(x=180, y=35)
botonRojo2 = Button(ventana, bg="red", width=2, height=2, command = lambda:color2(1)).place(x=105, y=125)
botonAzul2 = Button(ventana, bg="blue", width=2, height=2, command = lambda:color2(2)).place(x=130, y=125)
botonAmarillo2 = Button(ventana, bg="yellow", width=2, height=2, command = lambda:color2(3)).place(x=155, y=125)
botonVerde2 = Button(ventana, bg="green", width=2, height=2, command = lambda:color2(4)).place(x=180, y=125)
botonacepta=Button(ventana, text="Aceptar", command=botonAceptar).place(x=130, y=250)
labelCoor = Label(ventana, text="COORDENADAS:").place(x=110, y=190)
labelX = Label(ventana, text="X: ").place(x=110, y=220)
dimX = Entry(ventana)
dimX.place(x=130, y=220, width=20, height=20)
labelY = Label(ventana, text="Y: ").place(x=160, y=220)
dimY = Entry(ventana)
dimY.place(x=180, y=220, width=20, height=20)

# VENTANA PRINCIPAL
barraMenu = Menu(raiz)
mnArchivo = Menu(barraMenu)
mnArchivo.add_command(label="Abrir partida")
mnArchivo.add_command(label="Guardar partida")
mnArchivo.add_command(label="Ayuda", command = defayuda)
barraMenu.add_cascade(label="Menu", menu=mnArchivo)
raiz.config(menu=barraMenu)
frameMenu = Frame()
frameMenu.pack(side="left")
frameMenu.config(bg="darkgray")
frameMenu.config(width="250", height="1000")
botonIniciar = Button(frameMenu, text="Inicio de juego", command=abrirVentana).place(x=80, y=25)
botonReportes = Button(frameMenu, text="Reportes de juego").place(x=71, y=75)
frameTablero = Frame(raiz)
frameTablero.config(bg="LightSteelBLue")
frameTablero.place(relx=0.37, rely=0.08, width="500", height="500")
im = PhotoImage(file="gifinicio.gif")
lblImagen = Label(raiz, image=im)
lblImagen.place(x=370, y=46)



raiz.mainloop()


