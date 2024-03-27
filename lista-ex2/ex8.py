def contar_palavras(frase: str):
  contagem_palavras = {}

  for invalido in ("0", "1", "2", "3", "4", "6", "7", "8", "9", ".", ",", "/", "?", "!", "'"):
    frase = frase.replace(invalido, "")

  frase = frase.split(" ")

  for palavra in frase:
    palavra = palavra.replace(",", "")
    palavra = palavra.replace(".", "")

    contagem_palavras[palavra] = 0
    contagem_palavras[palavra] = frase.count(palavra)

  return contagem_palavras

frase = str(input("Digite uma frase para contar a quantidade de cada palavra utilizadas: "))
print(contar_palavras(frase))            

                            
