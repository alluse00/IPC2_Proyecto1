


def escribirArchivoXML(datos, ruta):
    try:
        elementoMatrices = ET.Element('matrices')
        matrizz = datos.head
        for i in range(0, datos.size):
            filaa = matrizz.matriz.head
            elementoMatriz = ET.SubElement(elementoMatrices, "matriz, nombre=matriz")
            while filaa is not None:
                dato = filaa.fila.head
                while dato is not None:
                    ET.SubElement(elementoMatriz, "dato", x=filaa.fila.x, y=dato.y)
                    dato = dato.next

                filaa = filaa.next

            filaa = matrizz.matriz.head
            while filaa is not None:
                ET.SubElement(elementoMatriz, "frecuencia", g=filaa.fila.x).text = frecuencia
                filaa = filaa.next

            matrizz= matrizz.next
        



        b_xml = ET.ElementTree(elementoMatrices)
        with open(ruta, "a") as f:
            f.write(b_xml)
        
        subprocess.Popen([ruta], shell=True)
    except:
        print("Algo ha sucedido")