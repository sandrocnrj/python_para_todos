# -*- coding: utf-8 -*-

"""
    O laço WHILE executa um determinado bloco de código enquanto a condição for verdadeira
    
    while <condição>:
        <bloco de código>
        continue
        break
    else:
        <bloco de código>
"""

m = 0
k = 1

while k < 100:
    m = m + k
    k = k + 1


print("A soma é: ", m)