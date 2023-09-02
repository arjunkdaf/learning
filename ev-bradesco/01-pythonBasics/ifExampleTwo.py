varA = input("Informe um valor para a variável A: ")
varB = input("Informe um valor para a variável B: ")

if varA > varB:
    aux = varA
    varA = varB
    varB = aux

print("O valor da variável A agora é:", varA)
print("O valor da variável B agora é:", varB)
