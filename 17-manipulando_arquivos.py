# -*- coding: utf-8 -*-

#Criando
temp = open("meu_arquivo.txt","w")

#Escrevendo
for i in range(100):
    temp.write('Linha: %i \n' % (i))

#Fechando
temp.close()