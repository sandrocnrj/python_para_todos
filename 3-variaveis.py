# -*- coding: utf-8 -*-
"""
    Python é uma linguagem dinamicamente tipada, ou seja: não é necessário tipar as variáveis antes de usá-las. 
    Por um processo chamado binding, quando se atribui um valor a variável ela já é tipada de acordo com o valor.
"""
msg = "Olá Mundo"
print(msg)

#Agora vamos verificar o tipo da variável
tipo = type(msg)
print(tipo)

"""
    Não foi preciso declarar a variável msg antes de utilizá-la. Agora vamos acrescentar um valor inteiro, 
e você vai perceber que não vai dar error, por que agora o tipo da variável passou a ser int.
"""
msg = "Olá Mundo"
print(msg)

msg = 3

#Agora vamos verificar o tipo da variável
tipo = type(msg)
print(tipo)

"""
    Os principais tipos de dados em Python são: inteiros, floats, strings, listas, tuplas e dicionários.
    O Python oferece alguns tipos numéricos na forma de builtins.

    Inteiro (int)
    Real de ponto flutuante (float)
"""

# variálvel de valor inteiro
v_inteiro = 10

# variável de ponto flutuante
v_real = 3.45

print("Inteiro : ", v_inteiro)
print("Ponto Flutuante : ", v_real)


"""
    Agora vamos converter de inteiro para real e de real para inteiro, nesse script:
"""

print("Convertendo de Inteiro para Real : ", float(v_inteiro))
print("Convertendo de Real para Inteiro : ", int(v_real))