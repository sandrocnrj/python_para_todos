# -*- coding: utf-8 -*-
#O operador % pode ser utilizado para fazer interpolação na string e com isso, formatar sua saída:

v_string = "Treinamento"
 
print("O tamanho de %s é %d " % (v_string, len(v_string)))
print("A string é %s " % v_string)

#%s para string
#%d para inteiro
#%f para float

#Entre outros.
#Os numéros podem ser inseridos após % para formatar a apresentação dos valores:

# Colocando zero a esquerda 
print("A hora é : %02d:%02d" % (7,45))

# Controle das casas decimais
print("A porcentagem é : %.2f%%" % (4.4555555555555555))