arch_cuentos = open('Cuentos.txt', encoding = "ISO-8859-1")
arch_arania_negra = open('La araña negra - tomo 1.txt', encoding = "ISO-8859-1")
# arch_settings = open('configuracion.txt','rb')
arch_1000_noches_y_1_noche = open('Las 1000 Noches y 1 Noche.txt', encoding = "ISO-8859-1")
arch_palabras = open('palabras.txt','w+')

linea_arch_cuentos = arch_cuentos.readline()
linea_arch_arania_negra = arch_arania_negra.readline()
# linea_arch_settings = arch_settings.readline()
linea_arch_1000_noches_y_1_noche = arch_1000_noches_y_1_noche.readline()


def leer_archivo(archivo):
    linea = archivo.readline()
    while linea:
        print(linea)
        linea = archivo.readline()

print(leer_archivo(arch_cuentos))


arch_cuentos.close()
arch_arania_negra.close()
# arch_settings.close()
arch_1000_noches_y_1_noche.close()
