import random
import sys
import time

numero = random.randint(1,6)

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, u"█"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()



print("\nJOGO DE DADOS!")

y = 0

while y == 0:
    print("1 - Jogar")
    escolha = int(input("\nEscolha: "))


    if escolha == 1:
        for i in progressbar(range(100), "Lançando: ", 50):
           time.sleep(0.00001)
#           print(numero)
        print("Número: " + str(numero))
        print("")
        exit()

    else:
        exit()