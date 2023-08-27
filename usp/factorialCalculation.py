num = int(input("Digite um número para fazer o cálculo fatorial: "))
fatorial = 1
i = 2

while i <= num:
    fatorial = fatorial * i
    i = i + 1
print("O resultado fatorial de", num, "é:", fatorial)

