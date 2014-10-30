# -*- coding: utf-8 -*-
"""
    As strings em Python também são tipos builtins.
    Temos dois tipos de strings disponíveis:

    String padrão
    String unicode

    A string padrão pode ser convertida para Unicode atravês da função unicode().
    A inicialização da string pode ser:

    Com aspas simples ou duplas
    Em várias linhas, desde seja entre aspas simples ou duplas

    Uma string é uma sequência de letras, endereçada de tal forma que você pode requisitar um valor qualquer dessa sequência e fazer o que quiser com ele.

    Como em qualquer sequência em Python, os endereçamentos começam a ser contatos do zero.
"""

v_string = "Treinamento"

print(v_string[0])

#Intervalo de String
#Podemos também solicitar um intervalo da sequência. 

v_string = "Treinamento"

print(v_string[6:9])

#Lembrando que os endereços se referem  aos intervalos entre os itens, e não o item em si:

#T R E I N A M E N T  O
#0 1  2 3 4 5  6   7 8  9  10

#v_string[6:9] retorna : MEN

#Pode-se omitir a posição da direita, se ela for a última:

print(v_string[6:])

#Ou pode-se omitir o da esquerda, se ele for a primeira posição da sua sequência:

print(v_string[:9])

#Se você não quiser todos os valores da string, poderá usar um incremento:

v_string = "Treinamento"

print(v_string[1:9:2])

#Com incremento negativo é possível varrer a string de trás para frente:

v_string = "Treinamento"

print(v_string[10:0:-1])

#Para concatenar duas strings use o operador +.

v_string = "Treinamento"

v_string = v_string + " Python"

print(v_string)

#Use a função len(x), para saber o tamanho de uma string.

v_string = "Treinamento"

v_string = v_string + " Python"
 
print("O tamanho da string: ",len(v_string))