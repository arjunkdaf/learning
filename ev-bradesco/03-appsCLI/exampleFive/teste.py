from area import Retangulo
import math

while True:
    pisoA = float(input('Digite um lado do piso: '))
    pisoB = float(input('Digite o outro lado do piso: '))

    piso = Retangulo(pisoA, pisoB)

    azA = float(input('Digite um lado do azulejo: '))
    azB = float(input('Digite o outro lado do azulejo: '))

    azulejo = Retangulo(azA, azB)

    areaPiso = piso.area()
    areaAzulejo = azulejo.area()

    qntdAz = areaPiso / areaAzulejo

    if areaPiso % areaAzulejo == 0:
        print(f'A quantidade exata de azulejos para preencher o piso é de {qntdAz}')
    else:
        print(f'A quantidade mínima de azulejos para preencher o piso é de {math.ceil(qntdAz)}')