string = str(input("Digite uma palavra ou uma frase para que verifique se é um palíndromo: "))

if string.lower() == string[::-1].lower():
  print("É um palíndromo")
else:
  print("Não é um palíndromo")
