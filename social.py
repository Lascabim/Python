import random

print("\nSOCIAL GAME")
print("Faz uma pergunta e eu respondo por ti :)")

print("""
1 - Jogar
2 - Parar
""")

y = 0

while y == 0:
    seguir = int(input("Continuar: "))
    print("")

    if seguir == 1:

        random = random.randint(1, 4)

        r1 = "Sim" 
        r2 = "Não"
        final = ""

        if random == 1:
            final = r1
        else:
            final = r2
       

        question = input("Pergunta: ")
        print(final + "\n")
    else:
        y = 1
        exit()
    

