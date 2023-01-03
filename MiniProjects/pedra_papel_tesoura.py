import random 

user_vitorias = 0
pc_vitorias = 0

options = ["pedra", "papel", "tesoura"]

while True:
    user_input = input("Escreve Pedra/Papel/Tesoura ou Q para saíres: ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(1, 3)
    # pedra: 1, papel: 2, tesoura: 3
    computer_pick = options[random_number]
    print("Escolha do PC", computer_pick + ".")

    if user_input == "pedra" and computer_pick == "tesoura":
        print("Ganhas-te!")
        user_vitorias += 1  
    
    elif user_input == "papel" and computer_pick == "pedra":
        print("Ganhas-te!")
        user_vitorias += 1

    elif user_input == "tesoura" and computer_pick == "papel":
        print("Ganhas-te!")
        user_vitorias += 1

    else:
        print("Perdes-te!")
        pc_vitorias += 1

print("Ganhas-te", user_vitorias,"vezes!")
print("O PC ganhou", pc_vitorias,"vezes!")
print("FIM")