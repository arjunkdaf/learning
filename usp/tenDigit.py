numero = int(input('Digite um número inteiro: '))
dezena = ((numero - (numero % 10)) // 10) % 10

print('O dígito das dezenas é', dezena)
