print( 6 * '--','Caluladora de Gorjetas', 6 * '--')

conta = float(input("Digite o valor da conta: "))
porcentagem = int(input("Digite a porcentagem de gorjeta que você gostaria de dar? 10 12 ou 15? "))
pessoas = int(input("Digite pessoas vão pagar a conta: "))

conta_com_gorjeta = porcentagem / 100 * conta + conta
final = conta_com_gorjeta / pessoas


print(f"Cada pessoa vai pagar {final}")



