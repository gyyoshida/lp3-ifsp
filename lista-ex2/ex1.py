from random import randint

random = randint(0, 100)
palpite = 0;

print("Iniciando o jogo de adivinhação!!!")
while palpite != random:
    palpite = int(input("Digite um número entra 0 a 100: "))
    if palpite == random:
        print(f"Parabéns, você venceu! O número era {random}")
        break;
    elif palpite > random:
        print(f"Você errou! Seu palpite está alto!")
    else:
        print(f"Você errou! Seu palpite está baixo!")

