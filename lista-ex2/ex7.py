from random import choice

print("---------------------------")
print("BEM-VINDO AO JOGO DA FORCA")
print("---------------------------")

palavras = (
    "clove",
    "geeko",
    "sage",
    "omen",
    "astra",
    "deadlock",
    "valorant"
)

palavra_oculta = choice(palavras).lower()
chute = ["_" for _ in palavra_oculta]
tentativas = 3
letras_tentadas = []

while tentativas > 0:
    print(f"Você tem {tentativas} tentativa(s)")
    print(" ".join(chute))

    if "".join(chute) == palavra_oculta:
        print("Você acertou!")
        break

    if letras_tentadas:
        print(f"\nÚltimo chute incorreto: "" ".join(letras_tentadas))
    letra_chute = input("Digite uma letra: ").lower()

    if letra_chute not in palavra_oculta:
        tentativas -= 1
        letras_tentadas.append(letra_chute)
        print("Letra incorreta!")
    else:
        for i in range(len(palavra_oculta)):
            if palavra_oculta[i] == letra_chute:
                chute[i] = letra_chute
else:
    print(f"Você não tem mais tentativas. A palavra era: {palavra_oculta}")
