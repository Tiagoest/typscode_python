print(6 * "--", "If e Else Aninhados", 6 * "--")

alt = int(input("Qual a sua altura? "))
conta = 0

if alt >= 120:

    print("Passagem autorizada")

    ano = int(input("Qual a sua idade? "))

    if ano < 12:
        conta = 5
        print("Sua passagem será R$5,00 reais!")

    elif ano <= 18:
        conta = 18
        print("Sua passagem será R$18,00 reais!")

        #45 <= idade <= 
    elif ano >= 45 and ano <= 55:
        conta = 0
        print("Pela sua idade elevada, sua passagem será R$0,00!")

    else:
        conta = 24
        print("Sua passagem será R$24,00 reais!")
    
    foto = str(input("Você quer tirar fotos? Responda com (s)sim e (n)não: "))

    if foto == "s":
        conta += 3
    
    print(f"O preço final foi R${conta}")

else:
    print("Passagem negada")
    