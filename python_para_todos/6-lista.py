# -*- coding: utf-8 -*-

"""
    Em Python as listas são mutáveis, podendo ser alteradas a qualquer momento.
    Lembrando que em Python os elementos iniciam em 0. Então para acessar o primeiro elemento da lista 
    é necessário informar o índice 0.
"""

lista = [1,3,5,7,9]

print(lista[2])

#Com o operador + pode-se também concatenar uma lista:

lista1 = [1,3,5,7,9]
lista2 = [11,13,15,17,19]

lista = lista1 + lista2

print(lista)

#Você poderá adicionar um elemento a lista de suas formas: concatenando o elemento a lista; ou com o método append():

lista = [1,3,5]

# Adicionando um elemento a lista concatenando listas
lista = lista + [7]

print(lista)

# Adicionando um elemento a lista usando o método append()
lista.append(9)

print(lista)

#O método append() adiciona um elemento ao final da lista. Caso você queira adicionar uma nova lista poderá usar o método extend():

lista = [1,3,5]

listax = [7,9]

lista.extend(listax)

print(lista)

#O Python lhe oferece as operações mais comuns para se trabalhar com listas:

lista = [1,3,5]

i = 2

# Incluindo um item
lista.append(7)

# Incluindo uma lista
lista.extend([9,11,13])

# Incluindo um item na posição i
lista.insert(i, 8)

# Remove um item 
lista.remove(13)

# Remove o item da posição i
lista.pop(i)

# Retorna o index do item 
print("Índice do item 5 => ", lista.index(5))
print("Número de vezes de 1 => ", lista.count(0))

# Ordena os itens da lista
lista.sort()

# Inverte a ordem dos itens da lista
lista.reverse()

#A melhor forma de mostrar os itens de uma lista e fazendo um FOR:
lista = ["verde","amarelo","azul","branco"]

for item in lista:
    print(item)
