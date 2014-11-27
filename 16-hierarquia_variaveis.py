# -*- coding: utf-8 -*-

def somalista(lista):
    """
        Somando lista recursivamente e colocando o resultado em uma variável global        
    """
    
    #soma = 10
    global soma
    
    for item in lista:
        if type(item) is list: #----> Se o tipo for lista
            somalista(item)
        else:
            soma += item

soma = 0
somalista([[1,2],[3,4,5],6])

print(soma)