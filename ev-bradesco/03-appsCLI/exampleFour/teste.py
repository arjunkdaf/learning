from funcionario import Funcionario

funcionario = Funcionario('Adilson', 'adilson@opensource.com')

funcionario.cadastroHora('Jan', 300)
funcionario.cadastroHora('Fev', 200)
funcionario.cadastroSalarioHora('Jan', 30)
funcionario.cadastroSalarioHora('Fev', 30)

print(funcionario)
print(funcionario.calculaSalario('Jan'))
print(funcionario.calculaSalario('Fev'))