print(13 * "--", "Minigame: Ilha do tesouro", 13 * "--")

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Bem-vindo(a) á ilha do tesouro")
print("Sua missão é encontrar o tesouro!\n")

escolha1 = str(input("Você está em uma encruzilhada, no caminho da esquerda tem um caminho por uma floresta sombria," \
"\nno caminho da direita tem um caminho já explorado com uma rota feita." \
"\n\nPara onde você quer ir? Digite (esquerda) ou (direita): ")).lower()

if escolha1 == "esquerda":
    print("A floresta faz sons entranhos mas nada de ruim ocorreu.\n")

    escolha2 = str(input("Seguindo pela floresta você encontra um rio que você pode cortar caminho." \
    "\n\nPara onde você quer ir? Digite (nadar) ou (andar): ")).lower()
    
    if escolha2 == "andar":
        print("O caminho segue como antes, silencioso e calmo.\n") 

        escolha3 = str(input("Você encontra uma parede de pedra com três portas," \
        " uma vermelha reluzente e chamativa," \
        " uma amarela e pouco brilhosa e uma azul e bela." \
        "\n\nPara onde você quer ir? Digite (vermelho) ou (amarelo) ou (azul): ")).lower
        
        if escolha3 == "amarela":
            print("Atravessando a porta simples, você escontra o ouro e a riqueza que tanto desejava. VItória!")

        elif escolha3 == "vermelho":
            print("A morte certa o encontrou ao atravessar a porta. Fim de Jogo")

        elif escolha3 == "azul":
            print("A morte certa o encontrou ao atravessar a porta. Fim de Jogo")
        
        else:
            print("Escolha inválida")

    elif escolha2 == "nadar":
        print("Jacarés comem você vivo. Fim de jogo.")
    
    else:
        print("Escolha inválida")
        

elif escolha1 == "direita":
    print("Um caminho já feito quer dizer que tem pessoas que usam ele, e essas pessoas te encontraram e mataram você. Fim de jogo.")

else:
    print("Escolha inválida")
