# -*- coding: utf-8 -*-
"""
   if <condição>:
        <bloco de código>
    elif <condição>:
        <bloco de código>
    else:
        <bloco de código>
    
    <condição> = sentença que será avaliada
    <bloco de código> = código que vai ser executado caso a condição seja satisfatória
    elif e esle = podemos ter vários elif para o mesmo if, mas deve existir apenas 1(um) else no final
    os parênteses são necessários caso você queira evitar ambiguidades 
"""

temp = input("Informe a temperatura:")
temp = int(temp)

if temp < 0:
    print("Está congelando!")
elif 0 <= temp <= 20:
    print("Está frio!")
elif 21 <= temp <= 25:
    print("Está bom!")
elif 26 <= temp <= 35:
    print("Está quente!")
else:
    print("Está muito quente!")