class Pessoa:
    # docstrings descrevendo a classe
    "Nova classe chamada Pessoa"
    idade = 31
    def saudacao(self):
        print("Olá pessoas!")

# output 31
print(Pessoa.idade)

# output <function Pessoa.saudacao at 0x7fc4d618af80>
# identificando a função com nome e id
print(Pessoa.saudacao)

# __ identificam constructors
# __doc__ chama a docstring
print(Pessoa.__doc__)

# criando um novo objeto da classe Pessoa
arjun = Pessoa()

print(arjun.idade)

# <bound method Pessoa.saudacao of <__main__.Pessoa object at 0x7f9d209571f0>>
print(arjun.saudacao)

# output Olá pessoas!
# arjun.saudacao() == Pessoa.saudacao(arjun)
arjun.saudacao() 


