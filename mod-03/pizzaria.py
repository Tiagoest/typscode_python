print(6 * "--", "Pizzaria Tispcde",6 * "--")

print("Bem vindo(a) a pizzaria Tipscode! \n")
print("Tabela de pizzas: \nPizza pequena - R$15,00 \nPizza média - R$20,00 \nPizza grande - R$25,00\n")

tamanho = str(input("Qual tamanho de pizza? Pequena(p) Média(m) Grande(g): "))
pepperoni = str(input("Vai querer adicional de pepperoni? Sim(s) Não(n): "))
queijo = str(input("Vai querer queijo extra? Sim(s) Não(n): "))

conta = 0

if tamanho == "p":
    conta += 15

elif tamanho == "m":
    conta += 20

elif tamanho == "g":
    conta += 25
else:
    print("Seleção de campo inválida")

if pepperoni == "s":
    if tamanho == "p":
        conta += 2
    else:
        conta += 3

if queijo == "s":
    conta += 1

print(f"O valor final da sua pizza será de R${conta}")

