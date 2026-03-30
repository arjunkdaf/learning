# este seria o arquivo main do projeto, os arquivos agora se comunicam
class Cliente:
    def __init__(self, name, phone):
        # adicionando _ antes do nome a classe fica protegida
        # _ depois ficaria publica e __ depois, privada
        self._nome = name
        self._telefone = phone

# get é usado para ler o valores interno e enviá-los como retorno da função
# set recebe argumento que serão atribuido a membros internos do objeto

def get_nome(self):
    return self._nome

def set_nome(self, nome):
    self._nome = name
