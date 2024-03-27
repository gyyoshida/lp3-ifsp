frase = str(input("Digite uma frase para contar a quantidade de vogais e consoantes: ")

vogais = ("a", "e", "i", "o", "u")
outros = ( "0", "1", "2", "3", "4", "6", "7", "8", "9", ".", ",", "/", "?", "!", "'", " ")

vogais_contador = 0
consoantes_contador = 0

for letra in frase:
  if letra.lower() in vogais:
    vogais_contador += 1
  elif not letra in outros:
    consoantes_contador += 1

print(f"Sua frase possui: {vogais_contador} vogal(is) e {consoantes_contador} consoante(s)")
