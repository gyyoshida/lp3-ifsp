comprimento = float(input("Digite o comprimento do aquário: "))
altura = float(input("Digite a altura do aquário: "))
largura = float(input("Digite a largura do aquário: "))

temperatura_desejada = float(input("Digite a temperatura desejada: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente: "))

def get_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

volume = get_volume(comprimento, altura, largura)

def get_filtragem_minima(volume):
    return 2 * volume, 3* volume

def get_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

print(f"Volume: {volume}")
print(f"Filtragem por hora mínima: {get_filtragem_minima(volume)[0]}L/h a {get_filtragem_minima(volume)[1]}L/h")
print(f"Potência do termostato necessária: {get_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)}W")

