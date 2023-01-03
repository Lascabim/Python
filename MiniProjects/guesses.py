import random

top_of_range = input("Introduz um número: ")

fails = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Introduz um número maior do que 0!")
        quit()
else:
    print("Introduz um número!")
    quit()

random = random.randint(1, top_of_range)

while True:
    fails += 1
    tentativa = input("Tenta adivinhar: ")
    if tentativa.isdigit():
        tentativa = int(tentativa)
    else:
        print("Introduz um número!")
        continue

    if tentativa == random:
        print("PARABÉNS! ACERTAS-TE \n")
        break
    elif tentaiva > random:
        print("Muito acima ...")
    else:
        print("Muito abaixo ...")

print("Acertas-te com", fails, "tentativas")
