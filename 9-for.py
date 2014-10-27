# -*- coding: utf-8 -*-

"""
    É a estrutura de repetição mais usada no Python.
    Durante a execução de um laço FOR a referência aponta para o primeiro elemento da sequência.
    O bloco de código processa o elemento correspondente.
    A cada interação a referência é atualizada para o próximo elemento da sequência.
    Break = interrompe o laço.
    Continue = Passa para a próxima intereção sem executar o código que vier após a condição.    
"""

s = 0
for x in range(1,10):
    s = s + x
    
print("A soma é: %d" %s)