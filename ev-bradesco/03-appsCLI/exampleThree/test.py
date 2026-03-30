from functions import *

tv = Televisor('SONY', 'SONY-123')
controle = ControleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print('A fabricante da TV é: ', tv.fabricante)
print('O modelo da TV é:', tv.modelo)
print('Canais disponíveis:', tv.lista_de_canais)
print('O canal atual é :', tv.canal_atual)
print('Volume atual:', tv.volume)

tv.aumentaVolume(46)
print('Volume atual:', tv.volume)