import platform
import random
import time

arch_cuentos = open('Cuentos.txt', encoding="ISO-8859-1")
arch_arania_negra = open('La araña negra - tomo 1.txt', encoding="ISO-8859-1")
arch_1000_noches_y_1_noche = open('Las 1000 Noches y 1 Noche.txt', encoding="ISO-8859-1")
arch_palabras = open('palabras.txt', 'w+')
palabras_validas_cuentos = open('palabras_texto_cuentos.txt', 'w+')
palabras_validas_arania_negra = open('palabras_texto_arania_negra.txt', 'w+')
palabras_validas_1000_noches_y_1_noche = open('palabras_texto_1000_noches_y_1_noche.txt', 'w+')
caracteres_reemplazar = open('reemplazar.txt', encoding="ISO-8859-1")

def sistemaOperativo():
    """Programada por Joaquín Andresen.
    Detecta el sistema operativo del usuario"""
    return platform.system()

def leer_archivo(archivo):
    linea = archivo.readline()
    lista = []
    while linea:
        if len(linea) > 1:
            listaPalabras = pasarTextoALista(linea)
            for palabra in listaPalabras:
                lista.append(palabra)
        linea = archivo.readline()
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
            reemplazar(palabra)
            palabra = palabra.upper()
            caract = es_texto_valido(palabra)
            num = any(caract == False for letra in palabra)
            if num is False and len(palabra) >= 5:
                if palabra in diccionario:
                    diccionario[palabra] += 1
                else:
                    diccionario[palabra] = 1
    return diccionario

def escribirArchivos(archivo_leer, archivo_escribir):
    """Programada por Joaquín Andresen.
    Recibe dos archivos, lee archivo_leer y crea un diccionario con sus palabras, luego procede a escribir el contenido
    del diccionario en archivo_escribir."""
    lista_de_palabras = leer_archivo(archivo_leer)
    diccionario_de_palabras = contar_palabras(lista_de_palabras)
    for palabra in sorted(diccionario_de_palabras.items(), key=lambda x: x[0]):
        if sistemaOperativo() == "Windows":
            archivo_escribir.write(palabra[0]+"\n")
        else:
            archivo_escribir.write((palabra[0]+"\n").encode('ascii', 'ignore').decode('ascii'))
    archivo_leer.seek(0)
    archivo_escribir.seek(0)

def reemplazar(palabra):
    linea = caracteres_reemplazar.readline()
    while linea:
        caracteres = linea.strip().split(",")
        palabra = palabra.replace(caracteres[0], caracteres[1])
        linea = caracteres_reemplazar.readline()
    return palabra


def leerLineaALinea(archivo, default):
    linea = archivo.readline()
    # print(linea)
    return linea if linea else default

def merge(archivo1, archivo2, archivo3, archivo_palabras):
    """Programada por Fernando Fabbiano.
     Merge entre los tres archivos que contienen los cuentos ya procesados, y ordenados alfabeticamente.
     Crea un único archivo llamada palabras, que contiene las palabras de los tres cuentos, sin repetir, y ordenadas
     alfabéticamente."""
    linea1 = leerLineaALinea(archivo1, "zzz")
    linea2 = leerLineaALinea(archivo2, "zzz")
    linea3 = leerLineaALinea(archivo3, "zzz")
    palabra1 = linea1.rstrip()
    palabra2 = linea2.rstrip()
    palabra3 = linea3.rstrip()
    while palabra1 != "zzz" or palabra2 != "zzz" or palabra3 != "zzz":
        palabratxt = arch_palabras
        leerLineaALinea(palabratxt, "zzz")
        lista = [palabra1, palabra2, palabra3]
        p1 = min(lista)
        if p1 not in palabratxt:
            palabratxt.write(p1 + "\n")
        if p1 == palabra1:
            linea1 = leerLineaALinea(archivo1, "zzz")
            palabra1 = linea1.rstrip()
        if p1 == palabra2:
            linea2 = leerLineaALinea(archivo2, "zzz")
            palabra2 = linea2.rstrip()
        if p1 == palabra3:
            linea3 = leerLineaALinea(archivo3, "zzz")
            palabra3 = linea3.rstrip()
    archivo1.seek(0)
    archivo2.seek(0)
    archivo3.seek(0)
    archivo_palabras.seek(0)

def total_palabras(archivo_palabras):
    linea = archivo_palabras.readline()
    cantidad_por_len = {}
    total = 0
    while linea:
        total += 1
        palabra = linea.strip()
        len_palabra = len(palabra)
        if str(len_palabra) not in cantidad_por_len:
            cantidad_por_len[str(len_palabra)] = 1
        else:
            cantidad_por_len[str(len_palabra)] += 1
        linea = archivo_palabras.readline()
    print("Hay " + str(total) + " palabras en total\n")
    time.sleep(1.0)
    for item in sorted(cantidad_por_len.items(), key=lambda x: int(x[0])):
        print("Hay " + str(item[1]) + " palabras de longitud: " + item[0])
        time.sleep(0.5)

def cantidad_jugadores():
    """Programada por Fernando Fabbiano.
    Solicita la cantidad de jugadores, y en el caso de que la respuesta no sea un entero,
    vuelve a pedir la cantidad"""
    cantidad = input("\nIngresar la cantidad de jugadores: ")
    while not cantidad.isdigit() or int(cantidad) > 10:
        cantidad = input("Error, ingrese una cantidad de jugadores menor o igual a 10: ")
    return int(cantidad)

def solicitar_nombres():
    """Programada por Fernando Fabbiano.
    Pide una cierta cantidad de nombres, basandose en la cantidad otorgada por la funcion cantidad_jugadores"""
    jugadores = []
    cantidad = cantidad_jugadores()
    for numero in range(1, cantidad+1):
        nombre = input("Ingrese el nombre del jugador "+str(numero)+": ").upper()
        jugadores.append(nombre)
    return jugadores

def random_jugadores():
    """Programada por Joaquín Andresen.
    Toma la lista de jugadores y la devuelve mezclada"""
    jugadores = solicitar_nombres()
    random.shuffle(jugadores)
    return jugadores

def solicitar_longitud():
    """Programada por Maximiliano Coppola.
    Solicita la longitud de la palabra a adivinar, y en caso de no ser una entero, vuelve a solicitar"""
    longitud = input("\nIngrese la longitud de la palabra a adivinar: ")
    while not longitud.isdigit() or int(longitud) < 5:
        longitud = input("\nError, ingrese una longitud mayor o igual a 5: ")
    return int(longitud)

def random_linea(archivo):
    linea = archivo.readline()
    for num, linea_random in enumerate(archivo):
        if random.randrange(num + 2): continue
        linea = linea_random
    archivo.seek(0)
    return linea

def random_palabra(longitud):
    palabra = random_linea(arch_palabras).strip()
    while len(palabra) != longitud:
        palabra = random_linea(arch_palabras).strip()
    arch_palabras.seek(0)
    return str(palabra)

def ingresar_letra(utilizadas):
    """Programada por Joaquín Andresen.
    Solicita una letra, y en caso de no ser un caracter válido, vuelve a solicitar"""
    letra = input("Ingrese una letra: ")
    while letra.isdigit() == True or len(letra) != 1 or letra in utilizadas:
        letra = input("Error, ingrese una letra valida: ")
    return letra.upper()

def mensaje_de_turno(datos, jugador):
    """Programada por Santiago Álvarez.
    Recibe el nombre de un jugador con sus datos, y muestra el mensaje de turno de ese jugador"""
    print("\n")
    print("Turno de " + str(jugador))
    print("".join(datos[jugador][6]), "Aciertos: " + str(datos[jugador][0]),
          "Desaciertos: " + str(datos[jugador][1]), "Puntos: " + str(datos[jugador][4]),
          "Letras utilizadas: " + str(datos[jugador][7]), "\n")

def ahorcado(jugadores, datos):
    """Programada por todos.
    Sistema de turnos, hace que cada jugador juegue hasta que se equivoque para pasar al siguiente,
    asi sucesivamente hasta que algun jugador adivine la palabra o todos superen el limite de desaciertos"""
    time.sleep(1.0)
    print("\nEl orden en que jugaran será:", ', '.join([jugador for jugador in jugadores]))
    longitud = solicitar_longitud()
    contador = 0
    datos1 = datos
    arch_palabras.seek(0)
    for jugador in jugadores:
        datos1[jugador][0] = 0
        datos1[jugador][1] = 0
        datos1[jugador][7] = []
        datos1[jugador][5] = random_palabra(longitud)
        datos1[jugador][6] = []
        datos1[jugador][8] = 0
        for y in datos1[jugador][5]:
            datos1[jugador][6].append("_")
    while contador/len(jugadores) != 8:
        for jugador in jugadores:
            if datos1[jugador][8] < 8:
                mensaje_de_turno(datos1, jugador)
                letra = ingresar_letra(datos1[jugador][7])
                datos1[jugador][8] += 1
                contador += 1
                if letra not in datos1[jugador][7]:
                    datos1[jugador][7].append(letra)
                while letra in list(datos1[jugador][5]) and "_" in datos1[jugador][6]:
                    datos1[jugador][4] += 1
                    for z in range(len(datos1[jugador][5])):
                        if letra == datos1[jugador][5][z]:
                            datos1[jugador][6][z] = letra
                    if "_" not in datos1[jugador][6]:
                        print("\n", "Felicidades " + jugador + ", has ganado!", "\n")
                        ganador = jugador
                        datos1[jugador][4] += 30
                        return datos1, ganador
                    if letra in list(datos1[jugador][5]):
                        datos1[jugador][0] += 1
                        datos1[jugador][2] += 1
                    mensaje_de_turno(datos1, jugador)
                    letra = ingresar_letra(datos1[jugador][7])
                    datos1[jugador][8] += 1
                    contador += 1
                    if letra not in datos1[jugador][7]:
                        datos1[jugador][7].append(letra)
                datos1[jugador][4] -= 2
                datos1[jugador][1] += 1
                datos1[jugador][3] += 1
    print("\n", "Ha ganado el programa", "\n")
    ganador = "CPU"
    return datos1, ganador

def main():
    """ Programada por todos.
    Funcion principal que junta todos los datos obtenidos y corre el juego. datos[0] son los aciertos de la partida,
    datos[1] son los desaciertos, datos[2] son los aciertos totales, datos[3] son los desaciertos totales,
    datos[4] son los puntos, datos[5] es la palabra a divinar, datos[6] es la palabra a davinar con los guiones bajos,
    datos[7] son las letras utilizadas, datos[8] es el contador de turnos de el jugador. """
    print("Bienvenidos al Ahorcado, desarrollado por: ")
    time.sleep(1.0)
    print(''' 
    _________             __                                            
    \_   ___ \_____      |__|____      ____   ____   ________________   
    /    \  \/\__  \     |  \__  \    /    \_/ __ \ / ___\_  __ \__  \  
    \     \____/ __ \_   |  |/ __ \_ |   |  \  ___// /_/  >  | \// __ \_
     \______  (____  /\__|  (____  / |___|  /\___  >___  /|__|  (____  /
            \/     \/\______|    \/       \/     \/_____/            \/ ''', end=" ")
    time.sleep(1.0)
    print("v2.0\n")
    time.sleep(1.0)
    escribirArchivos(arch_cuentos, palabras_validas_cuentos)
    escribirArchivos(arch_arania_negra, palabras_validas_arania_negra)
    escribirArchivos(arch_1000_noches_y_1_noche, palabras_validas_1000_noches_y_1_noche)
    merge(palabras_validas_cuentos, palabras_validas_arania_negra, palabras_validas_1000_noches_y_1_noche,
          arch_palabras)
    total_palabras(arch_palabras)
    time.sleep(1.0)
    jugadores = random_jugadores()
    seguir = 1
    valido = [0, 1]
    datos = {}
    partidas_jugadas = 0
    for jugador in jugadores:
        datos[jugador] = [0, 0, 0, 0, 0, "", [], [], 0]
    while seguir:
        partidas_jugadas += 1
        datos, ganador = ahorcado(jugadores, datos)
        print("Resultados Generales:")
        for jugador in jugadores:
            print("Datos de " + jugador, "\n", "Palabra: " + datos[jugador][5], "\n", "Puntaje: " + str(datos[jugador][4]),
                  "\n", "Aciertos: " + str(datos[jugador][2]), "\n", "Desaciertos: " + str(datos[jugador][3]), "\n")
        if partidas_jugadas > 1:
            print("Partidas Jugadas: " + str(partidas_jugadas))
        jugadores.clear()
        if ganador == "CPU":
            for item in sorted(datos.items(), key=lambda y: y[1][4], reverse=True):
                jugadores.append(item[0])
        else:
            jugadores.append(ganador)
            for item in sorted(datos.items(), key=lambda y: y[1][4], reverse=True):
                if item[0] != ganador:
                    jugadores.append(item[0])
        seguir = input("Desea jugar otra partida? (0 = no, 1 = si) ")
        if not seguir.isdigit() or int(seguir) not in valido:
            seguir = input("Error, ingrese 1 para continuar y 0 para finalizar la partida: ")
        seguir = int(seguir)
        arch_palabras.seek(0)
    print("El juego ha finalizado")

main()

arch_cuentos.close()
arch_arania_negra.close()
arch_1000_noches_y_1_noche.close()
arch_palabras.close()
palabras_validas_1000_noches_y_1_noche.close()
palabras_validas_cuentos.close()
palabras_validas_arania_negra.close()
caracteres_reemplazar.close()