# -*- coding: utf-8 -*-
import time

#LOCALTIME = vai retornar a data e hora local (struct_time)
print(time.localtime())

#ASCTIME = vai retornar a data e hora como string
print(time.asctime())

#TIME = vai retornar o tempo do sistema em segundos
tempo_segundo1 = time.time()

#GMTIME = função que converte segundos para struct_time
tempo1 = time.gmtime(tempo_segundo1)
print(tempo_segundo1, '=>', tempo1)


#Vamos somar uma hora
tempo2 = time.gmtime(tempo_segundo1 + 3600)

#MKTIME = função que converte de struct_time para segundos
tempo_segundo2 = time.mktime(tempo2)
print(tempo_segundo2, '=>', tempo2)

#CLOCK = retorna o tempo em segundos, desde quando o sistema se iniciou
print('O sistema demorou ', time.clock(), ' segundos até agora.')

#Agora vamos contar os segundos
for i in range(5):
    #SLEEP = função que executa uma pausa mediante ao número de segundos especificados
    time.sleep(1)
    print(i + 1, 'segundo(s)')
