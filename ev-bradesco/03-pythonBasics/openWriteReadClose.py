# gravando um arquivo com 'w' na mesma pasta, com nome openCloseWrite.txt
teste = open("openWriteReadClose.txt", "w")

# adicionando texto ao arquivo
teste.write("Curso Python EV-Bradesco \n")
teste.write("Aula prática - Módulo Python básico")

# fechar o arquivo garante que os recursos do sistema sejam liberados
# e também que o arquivo não seja corrompido
teste.close()

# lendo o conteudo do arquivo
leitura = open("openWriteReadClose.txt", "r")
print(leitura.read())
leitura.close()

# Parâmetros do open()
# "r" abre o arquivo somente para leitura; ele já deve existir
# "r+" abre para leitura e escrita; o arquivo deve existir; a escrita começa na primeira linha; caso exista algum dado, será reescrito conforme formos escrevendo
# "w" abre o arquivo no início somente para escrita; cria um novo se não existir e apagará o conteúdo caso exista
# "w+" abre para escrita e leitura, apagando o que existir
# "a" abre para escrita no final do arquivo; não apaga o conteúdo existente
# "a+" abre para escrita e leitura no final do arquivo

