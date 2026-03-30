totalSegundos = int(input('Entre com o número de segundos que deseja converter: '))

milenios = totalSegundos // 29030400000
segundosRestantes = totalSegundos % 29030400000
centenios = segundosRestantes // 2903040000
segundosRestantes = segundosRestantes % 2903040000
decadas = segundosRestantes // 290304000
segundosRestantes = segundosRestantes % 290304000
anos = segundosRestantes // 29030400
segundosRestantes = segundosRestantes % 29030400
meses = segundosRestantes // 2419200
segundosRestantes = segundosRestantes % 2419200
semanas = segundosRestantes // 604800
segundosRestantes = segundosRestantes % 604800
dias = segundosRestantes // 86400
segundosRestantes = segundosRestantes % 86400
horas = segundosRestantes // 3600
segundosRestantes = segundosRestantes % 3600
minutos = segundosRestantes // 60
segundosRestantesFinais = segundosRestantes % 60

print(milenios, 'milênio(s),', centenios, 'centênio(s),', decadas, 'década(s),', anos, 'ano(s),', meses, 'mês(es),', semanas, 'semana(s),', dias, 'dia(s),', horas, 'hora(s),', minutos, 'minuto(s) e', segundosRestantesFinais, 'segundo(s).')
