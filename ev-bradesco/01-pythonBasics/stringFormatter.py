codigo = 105
nome = 'José Santana'
salario = 2800.00
ativo = True

# o caractere % formata uma variavel dentro da string
# %d ou %i para valores inteiros
# %f para valores decimais, com padrão de quatro casas pós vírgula
# %.1f para uma casa %.2f para duas, etc.
# %ld para números inteiros longos
# %e ou %E para número exponencial
# %c para caractere
# %o para número inteiro octal
# %x ou %X para número inteiro hexadecimal
# %s para string
# e %r para boolean

print("Código: %d "% codigo)
print("Nome: %s "% nome)
print("Salário: %.2f "% salario)
print("Ativo: %r "% ativo)

# inserindo caracteres com \
# \n	Insere uma quebra de linha.
# \t	Insere tabulação horizontal.
# \v	Insere tabulação vertical.
# \r	Equivalente ao efeito da tecla Enter.
# \’	Aspas simples.
# \”	Aspas duplas.
# \\	Insere uma barra invertida (backslash).
# \a	Chamado de ASC bell ou beep do sistema. Se houver suporte, aciona um bipe.
# \b	Aciona o backspace, ou seja, apaga o caractere anterior.
# \f	Insere uma quebra de página.
# \u	Insere um caractere UNICODE. Deve acompanhar um código com 4 números.