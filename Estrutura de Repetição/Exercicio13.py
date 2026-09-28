# gere um número aleatório de 1 a 100 e peça ao usuário para adivinhar, dando dicas de "maior" ou "menor" atéacertar. 

import random
numero_aleatorio = random.randint(1, 100)
tentativa = 0
while True:
    palpite = int(input("Adivinhe o número entre 1 e 100: "))
    tentativa += 1
    if palpite < numero_aleatorio:
        print("Tente um número maior.")
    elif palpite > numero_aleatorio:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativa} tentativas.")
        break
    
