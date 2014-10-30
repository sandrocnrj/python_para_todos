# -*- coding: utf-8 -*-

"""
    O comando BREAK serve para parar um processo WHILE ou FOR.
"""

num = int(input("Informe um numero:"))

primo = 0

for i in range(2,num):
    if num % i == 0:
        primo = 1
        print("Numero não é primo")
        break
    
if primo == 0:
    print("É primo!")