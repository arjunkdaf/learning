print('Digite uma sequência de valores a serem somados terminada por zero.')
soma = 0
valor = 1

while valor != 0:
    valor = float(input('Digite um valor: '))
    soma = soma + valor

print('A soma dos valores digitados é:', soma)

