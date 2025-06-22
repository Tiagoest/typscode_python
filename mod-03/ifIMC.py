print(6 * "--", "Calculadora de IMC", 6 * "--")

alt = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (alt ** 2)

print(round(imc, 1))

if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc >= 18.5 and imc <= 25:
    print("Você está no peso ideal!")
else:
    print("Você está acima do peso!")

