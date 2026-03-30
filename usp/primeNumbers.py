num = int(input("Digite o número inteiro que quer verificar se é primo: "))
div = 2
primo = True

while div < num and primo:
    if num % div == 0:
        primo = False
    div = div + 1

if primo and num != 1:
    print("O número", num, "é primo.")
else:
    print("O número ", num, "não é primo.")

