#><
import random 
import sys
import time

numero = random.randint(1,20)
attempts = 5

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


print("\nJogo da Adivinha\n")

for i in progressbar(range(100), "Gerando Número: ", 50):
           time.sleep(0.0000001)

print("\nTenta adivinhar o número gerado de 1 a 20: ")
print("Tens 5 tentativas!\n")

y = 0

while y == 0:
    num = int(input("Escolha: "))

    if attempts > 1:
        if num == numero:
            y = 1
            print("PARABÉNS, ADIVINHAS-TE!")
            exit()
        elif num > numero:
            print("O número é menor do que " + str(num))
            attempts = attempts - 1
        elif num < numero:
            print("O número é maior do que " + str(num))
            attempts = attempts - 1
    else:
        print("Ficas-te sem chances!")
        y = 1
