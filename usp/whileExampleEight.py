numSalvo = num = int(input("Digite um valor inteiro para verificar se existem dígitos adjascentes iguais: "))

anterior = num % 10
num = num // 10
iguais = False
pos = 0

while num > 0 and not iguais:
    atual = num % 10
    if atual == anterior:
        iguais = True
    else:
        pos = pos + 1
    anterior = atual
    num = num // 10

if iguais:
    print(numSalvo, "tem dois dígitos", atual, "adjacentes")
else:
    print(numSalvo, "não tem dígitos iguais adjacentes")

