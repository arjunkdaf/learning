idade = int(input("Digite a idade da pessoa: "))
if idade >= 18:
    print("A pessoa é maior de idade.")
elif idade < 18 and idade > 14:
    print("A pessoa é um menor da puberdade")
else:
    print("A pessoa é menor de idade.")