import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

maiuscula = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

simbolos = [ '!', '@', '#', '$', '+', '-', '*', '/', '.', ',']

n_letras = int(input('Digite quantas letra sua senha vai ter: \n'))
n_numeros = int(input('Digite quantas números sua senha vai ter: \n'))
n_simbolos = int(input('Digite quantas simbolos sua senha vai ter: \n'))

letras_selec = []
numeros_selec = []
simbolos_selec = []

todos_juntos = []

for ls in range(n_letras):
    l = random.choice(letras)
    letras_selec.append(l)

for ns in range(n_numeros):
    n = random.choice(numeros)
    numeros_selec.append(n)

for ss in range(n_simbolos):
    s = random.choice(simbolos)
    simbolos_selec.append(s)

todos_juntos.extend(letras_selec + numeros_selec + simbolos_selec)
random.shuffle(todos_juntos)

print('\nSENHA FINAL:',''.join(todos_juntos))
