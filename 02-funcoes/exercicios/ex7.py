peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

def get_IMC(peso, altura):
    return peso / altura ** 2

imc = get_IMC(peso, altura)

def get_classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    if imc < 25.0:
        return "Peso normal"
    if imc < 30.0:
        return "Excesso de peso"
    if imc < 35.0:
        return "Obesidade de Classe 1"
    if imc < 40.0:
        return "Obesidade de Classe 2"
    
    return "Obesidade de Classe 3"

def get_peso_ideal(peso, altura):
    return peso - (24.9 * altura * altura)

peso_ideal = get_peso_ideal(peso, altura)

print(f"IMC: {imc}")
print(f"Classificação: {get_classificacao(imc)}")

if peso_ideal >= 0.0:
    print(f"Você precisa perder {peso_ideal}Kg para atingir seu peso normal")
else:
    print(f"Você precisa ganhar {peso_ideal * -1}Kg para atingir seu peso normal")

