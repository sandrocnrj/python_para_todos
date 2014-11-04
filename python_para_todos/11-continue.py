# -*- coding: utf-8 -*-

"""
    O comando CONTINUE é usado para forçar a execução do laço soltar para a próxima interação.
"""

x = 0
while x <= 10:
    x = x + 1
    if x == 5:
        print("Não vamos imprimir o numero 5")
        continue
    print("x = ", x)