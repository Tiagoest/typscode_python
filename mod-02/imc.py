print(6 * "-", "Calculo de IMC", 6 * "-")

peso = float(input("Diigte seu peso: "))
altura = float(input("Digite seu altura: "))

IMC = peso / (altura ** 2)

print(f"Seu IMC é {int(IMC)}")
