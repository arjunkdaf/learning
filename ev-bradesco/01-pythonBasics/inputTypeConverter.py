codigo = int(input("Digite o códigodo funcionário: "))
# o input por padrão já recebe string então no caso abaixo não precisa converter
nome = input("Digite o nome do funcionário: ")
salario = float("Digite o valor do salário: ")
ativo = True

print("Código: %d "% codigo)
print("Nome: %s "% nome)
print("Salário: %.2f "% salario)
print("At\"ivo: %r "% ativo)