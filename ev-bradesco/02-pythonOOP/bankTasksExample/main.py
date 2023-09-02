class Main:
    pass # usado quando dentro da classe não se faz nada

from cliente import Cliente # do exemplo cliente.py
from conta import Conta 

c1 = Cliente("João", "98765-4321") # todos os atributos do exemplo um
conta = Conta(c1.nome, 4321,0)

print(c1)
print(c1.nome, "e", c1.telefone)
print(conta.titular, "Número:", conta.numero, "Seu saldo:", conta.saldo)
