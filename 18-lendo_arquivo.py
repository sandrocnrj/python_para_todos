# -*- coding: utf-8 -*-

#Abrindo
temp = open("meu_arquivo.txt","r")

#Lendo
#for linha in temp:
#    print(linha)

print(temp.readlines())

#Fechando    
temp.close()