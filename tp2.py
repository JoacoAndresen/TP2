arch_cuentos = open('Cuentos.txt', encoding="ISO-8859-1")
arch_arania_negra = open('La araña negra - tomo 1.txt', encoding="ISO-8859-1")
# arch_settings = open('configuracion.txt','rb')
arch_1000_noches_y_1_noche = open('Las 1000 Noches y 1 Noche.txt', encoding="ISO-8859-1")
arch_palabras = open('palabras.txt', 'w+')
palabras_validas_cuentos = open('palabras_texto_cuentos.txt', 'w+')
palabras_validas_arania_negra = open('palabras_texto_arania_negra.txt', 'w+')
palabras_validas_1000_noches_y_1_noche = open('palabras_texto_1000_noches_y_1_noche.txt', 'w+')


linea_arch_cuentos = arch_cuentos.readline()
linea_arch_arania_negra = arch_arania_negra.readline()
# linea_arch_settings = arch_settings.readline()
linea_arch_1000_noches_y_1_noche = arch_1000_noches_y_1_noche.readline()



def leer_archivo(archivo):
    linea = archivo.readline()
    lista = []
    while linea:
        #print(linea)
        linea = archivo.readline()
        if len(linea) > 1:
            listaPalabras = pasarTextoALista(linea)
            for palabra in listaPalabras:
                lista.append(palabra)
    lista.sort()
    return lista


def pasarTextoALista(lineaTexto):
    listaPalabras = lineaTexto.split()
    return listaPalabras


def es_texto_valido(palabra):
    """Programada por Maximiliano Coppola.
    Checkea si la palabra contine algun caracter no valido"""
    if palabra == "":
        return False
    for letra in palabra:
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúüvwxyz" or letra.isdigit() == True:
            return False
    return True


def contar_palabras(lista):
    """ Devuelve un diccionario formado por todas las palabras validas del texto y su cantidad de repeticiones. """
    diccionario = {}
    for renglon in lista:
        palabras = renglon.split()
        for palabra in palabras:
            palabra = palabra.lower()
            palabra = palabra.replace("á", "a")
            palabra = palabra.replace("é", "e")
            palabra = palabra.replace("í", "i")
            palabra = palabra.replace("ó", "o")
            palabra = palabra.replace("ú", "u")
            palabra = palabra.replace("ü", "u")
            palabra = palabra.upper()
            caract = es_texto_valido(palabra)
            num = any(caract == False for letra in palabra)
            if num is False and len(palabra) >= 5:
                if palabra in diccionario:
                    diccionario[palabra] += 1
                else:
                    diccionario[palabra] = 1
    return diccionario


lista_de_palabras_cuentos = leer_archivo(arch_cuentos)
lista_de_palabras_1000_noches_y_1_noche = leer_archivo(arch_1000_noches_y_1_noche)
lista_de_palabras_arania_negra = leer_archivo(arch_arania_negra)
diccionario_cuentos = contar_palabras(lista_de_palabras_cuentos)
palabras_cuentos = diccionario_cuentos.items()
#apariciones_palabras_cuentos = diccionario_cuentos.values()
for palabra in palabras_cuentos:
    palabras_validas_1000_noches_y_1_noche.write(palabra[0]+", "+str(palabra[1])+"\n")
print("Datos guardados exitosamente!")


arch_cuentos.close()
arch_arania_negra.close()
# arch_settings.close()
arch_1000_noches_y_1_noche.close()
arch_palabras.close()
