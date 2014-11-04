# -*- coding: utf-8 -*-

"""
    Funções são blocos de códigos identificados por um nome, que podem ou não receber parâmetros pré-determinados, 
    que serão usado em outras partes do código.

    def funcao(param1, param2=valor):
        <bloco de código>
        return valor
"""

def soma(vrl1, vrl2):
    return vrl1 + vrl2

#para chamar a função é só seguir o código abaixo
resultado = soma(2,3)

print("O resultado da soma 2 + 3 = ", resultado)

def rgb_html(r=0,g=0,b=0):
    """Converte R, G, B em #RRGGBB"""
    return '#%02x%02x%02x' % (r,g,b)

print(rgb_html(200,255))
print(rgb_html(b=200,r=255,g=100))

"""
    Existem formas de se definir funções que trabalhem com um número indefinido de argumentos.
    
    def func(*param):
        <bloco de código>
"""

def somatoria(*arg):
    """Soma de todos os argumentos"""
    soma = 0
    for i in arg:
        soma+= i
        
    return soma

#Agora você pode chamar a função passando quantos argumentos você achar necessário.
print(somatoria(2,4,6,8,10))

"""
    Também pode se passar os atributos, como se fossem um dicionário.
    
    def func(**param):
        <bloco de código>
"""

def func(**param):
    print(param)
    
func(s='Carvalho',n='Sandro')

