valor = float(input("Entre com o valor da sua compra: "))

if valor <= 9.99:
    print(f"O valor final é {valor}, foi aplicado 0% de desconto")

elif valor <= 99.99:
    valor -= valor * 0.05
    print(f"O valor final é {valor}, foi aplicado 5% de desconto")

elif valor <= 499.99:
    valor -= valor * 0.10
    print(f"O valor final é {valor}, foi aplicado 10% de desconto")

else:
    valor -= valor * 0.15
    print(f"O valor final é {valor}, foi aplicado 15% de desconto")
