print(6 * "--", "If e Else Aninhados", 6 * "--")

alt = int(input("Qual a sua altura? "))

if alt >= 120:
    print("Passagem autorizada")
    ano = int(input("Qual a sua idade? "))
    if ano < 12:
        print("Sua passagem será R$5,00 reais")
    elif ano <= 18:
        print("Sua passagem será R$12,00 reais")
    else:
        print("Sua passagem será R$24,00 reais")
else:
    print("Passagem negada")
    