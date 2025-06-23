print(6 * "--", "Minigame: Ilha do tesouro", 6 * "--")

print("Bem-vindo(a) á ilha do tesouro")
print("Sua missão é encontrar o tesouro!\n")

escolha1 = str(input("Você está em uma encruzilhada, no caminho da esquerda tem um caminho por uma floresta sombria," \
"\nno caminho da direita tem um caminho já explorado com uma rota feita." \
"\n\nPara onde você quer ir? Digite (esquerda) ou (direita): "))

if escolha1 == "esquerda":
    print("A floresta faz sons entranhos mas nada de ruim ocorreu.\n")

    escolha2 = str(input("Seguindo pela floresta você encontra um rio que você pode cortar caminho." \
    "\n\nPara onde você quer ir? Digite (nadar) ou (andar): "))
    
    if escolha2 == "andar":
        print("O caminho segue como antes, silencioso e calmo.\n") 

        escolha3 = str(input("Você encontra uma parede de pedra com três portas," \
        " uma vermelha reluzente e chamativa," \
        " uma amarela e pouco brilhosa e uma azul e bela." \
        "\n\nPara onde você quer ir? Digite (vermelho) ou (amarelo) ou (azul): "))
        
        if escolha3 == "amarela":
            print("Atravessando a porta simples, você escontra o ouro e a riqueza que tanto desejava. VItória!")

        else:
            print("A morte certa o encontrou ao atravessar a porta. Fim de Jogo")
    else:
        print("Jacarés comem você vivo. Fim de jogo.")

else:
    print("Um caminho já feito quer dizer que tem pessoas que usam ele, e essas pessoas te encontraram e mataram você. Fim de jogo.")
