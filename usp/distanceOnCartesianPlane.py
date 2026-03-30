import math

coordXUm = float(input('Digite o X da primeira coordenada: '))
coordYUm = float(input('Digite o Y da primeira coordenada: '))
coordXDois = float(input('Digite o X da segunda coordenada: '))
coordYDois = float(input('Digite o Y da segunda coordenada: '))

distancia = math.sqrt(((coordXUm - coordXDois) ** 2) + ((coordYUm - coordYDois) ** 2))

if distancia >= 10:
    print('É longe.')
else:
    print('É perto')

