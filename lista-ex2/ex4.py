candidato1 = 0
candidato2 = 0
candidato3 = 0

eleitores = int(input("Digite o número de eleitores: "))
for i in range(eleitores):
    voto = int(input(f"Digite o numero (1/2/3) correspondente do candidato em quem o eleitor {i + 1} quer votar: "))
   
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("Voto inválido")

print("Votação encerrada!!|\n")
print(f"Candidato 1: {candidato1} voto(s)\n")
print(f"Candidato 2: {candidato2} voto(s)\n")
print(f"Candidato 3: {candidato3} voto(s)\n")

if candidato1 > candidato2 and candidato1 > candidato3:
    print(f"O Candidato 1 foi eleito")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print(f"O Candidato 2 foi eleito")
elif candidato3 > candidato1 and candidato3 > candidato2:
    print(f"O Candidato 3 foi eleito")
else:
    print("Houve um empate")
