print('Digite uma sequência de valores a serem multiplicados terminada por um.')
multiplicacao = 1
valor = 0

while valor != 1:
    valor = float(input('Digite um valor: '))
    multiplicacao = multiplicacao * valor

print('A multiplicação dos valores digitados é:', multiplicacao)

