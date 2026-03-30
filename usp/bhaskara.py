import math

coefA = float(input('Digite o valor do coeficiente A: '))
coefB = float(input('Digite o valor do coeficiente B: '))
coefC = float(input('Digite o valor do coeficiente C: '))

delta = (coefB ** 2) - (4 * coefA * coefC)

if delta < 0:
    print('Não existem raízes reais para esta equação.')
elif delta == 0:
    deltaZero = (- coefB) / (2 * coefA)
    print('O valor da raiz é:', deltaZero)
else:
    deltaPositivoUm = ((- coefB) + math.sqrt(delta)) / (2 * coefA)
    deltaPositivoDois = ((- coefB) - math.sqrt(delta)) / (2 * coefA)
    print('Os valores das raízes são:', deltaPositivoUm, 'e', deltaPositivoDois)

