num = int(input('Digitar um número inteiro para que os dígitos sejam somados: '))
soma = 0

while num > 0:
    digito = num % 10
    num = num // 10
    soma = soma + digito
    
print('A soma dos dígitos é:', soma)
