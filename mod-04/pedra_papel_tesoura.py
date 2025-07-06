print(6 * '--', 'Pedra, Papel ou Tesoura!', 6 * '--')

import random

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

imagens_game = [pedra, papel, tesoura]

pc = random.randint(0,2)

escolha = int(input('''Pedra = 0
Papel = 1
Tesoura = 2

Faça sua escolha: '''))

if escolha >= 0 and escolha <= 2:
    print('\nSua escolha:')
    print(imagens_game[escolha])

    if escolha == 0: #PEDRA
        print('Escolha do computador:')
        print(imagens_game[pc])
        if pc == 0:
            print('\nEmpate!')
        elif pc == 1:
            print('\nDerrota!')
        else:
            print('\nVitória')

    elif escolha == 1: #PAPEL
        print('Escolha do computador:')
        print(imagens_game[pc])
        if pc == 0:
            print('\nVitória')
        elif pc == 1:
            print('\nEmpate!')
        else:
            print('\nDerrota!')

    elif escolha == 2: #TESOURA
        print('Escolha do computador:')
        print(imagens_game[pc])
        if pc == 0:
            print('\nDerrota!')
        elif pc == 1:
            print('\nVitória')
        else:
            print('\nEmpate!')

else:
    print('Erro, escolha inválida.')


