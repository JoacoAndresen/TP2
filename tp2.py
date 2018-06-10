arch_stories = open('Cuentos.txt','rb')
arch_black_spider = open('La araña negra - tomo 1.txt','rb')
arch_settings = open('configuracion.txt','rb')
arch_a_thousand_nights = open('Las 1000 Noches y 1 Noche.txt','rb')

linea_arch_stories = arch_stories.readline()
linea_arch_black_spider = arch_black_spider.readline()
linea_arch_settings = arch_settings.readline()
linea_arch_a_thousand_nights = arch_a_thousand_nights.readline()

def read_file(file):
    line = file.readline()
    while line:
        print(line)
        line = file.readline()

read_file(arch_stories)


arch_stories.close()
arch_black_spider.close()
arch_settings.close()
arch_a_thousand_nights.close()
