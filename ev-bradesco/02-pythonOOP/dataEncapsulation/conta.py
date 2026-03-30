class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero        
        self._saldo = 0

        # get é usado para ler o valores interno e enviá-los como retorno da função
        # set recebe argumento que serão atribuido a membros internos do objeto
        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, saldo):
            if saldo < 0:
                print("O saldo não pode ser negativo.")
            else:
                self._saldo = saldo