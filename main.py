
if __name__ == '__main__':
    op = 0

    while op != 6:
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo de salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Salida")
        op = int(input("Ingrese una opción: "))
        if op == 1:
            print("Opción Cargar archivo:")
            ruta=input("Ingrese la ruta\n")
            datos=LXML.leerArchivo(ruta)
            datos.imprimir()
        elif op == 2:
            print("Opción Procesar archivo:")
        elif op == 3:
            print("Opción Escribir archivo de salida:")
        elif op == 4:
            print("Opción Mostrar datos del estudiante:")
        elif op == 5:
            print("Opción Generar gráfica:")
    print("Adiós")
