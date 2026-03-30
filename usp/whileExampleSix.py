decrescente = True
quantidade = int(input("Digite a quantidade de números que a sequência terá: "))
anterior = int(input("Digite o primeiro número da sequência: "))
i = 0
valor = 0

while i < quantidade and decrescente:
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor
    i = i + 1

if decrescente:
    print("A sequência é decrescente.")
else:
    print("A sequência não é decrescente.")

