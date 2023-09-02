nums = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor > 0.0: # tem que ser positivo
    soma += valor
    nums += 1
    # nova entrada de valores
    valor = float(input("Digite um valor: "))
# digitando valor negativo o laço encerra

media = soma / nums

print("\nTotal da Soma:", soma)
print("\nQuantidade de valores digitados:", nums)
print("\nMédia dos valores:", media, "\n")
