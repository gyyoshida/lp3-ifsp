pontuacao = float(input("Digite sua pontuação de 0 a 100: "))

def converter_pontuacao(pontuacao):
    
    if pontuacao < 0.0 or pontuacao > 100.0:
        return "Pontuação inválida"
    elif pontuacao >= 90.0:
        return "A"
    elif pontuacao >= 80.0:
        return "B"
    elif pontuacao >= 70.0:
        return "C"
    elif pontuacao >= 60.0:
        return "D"
    else:
        return "F"
        
print(f"Sua nota convertida é: {converter_pontuacao(pontuacao)}")
