# -*- coding: utf-8 -*-

"""
    Se você possui uma sequência e precisa aplicar uma função sobre cada um dos seus termos, poderá utilizar algumas funções de builtin do Python.    
"""

def quadrado(elemento):
    return elemento**2

sequencia = [1,2,3,4,5,6]

resultado = list(map(quadrado,sequencia))

print(resultado)

"""
    No primeiro parâmetro da função map() encontra-se a função quadrado, que irá retornar o quadrado do elemento, no segundo parâmetro há a sequência 
    que será aplicada a função.
    
    Também pode ser utilizada a função que não executa operações algébricas
"""

def cambio(componente):
    print(componente[0],'R$ ', componente[1])
    print(componente[0],'US$ ', componente[1]*2.5)
    print('\n')
    
orcamento = {'asa':1200, 'combustivel':200, 'motor':4500}

print(list(map(cambio,orcamento.items())))