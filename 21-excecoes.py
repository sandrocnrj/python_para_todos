# -*- coding: utf-8 -*-
import traceback

#def divisao(x,y):
#    try:
#        resultado = x / y
#    except ZeroDivisionError:
#        print("Error ao tentar dividir por zero!")
#    else:
#        print("Resultado:", resultado)
#    finally:
#        print("Finally executado!")

list = []
for i in range(3):
    while 1:
        try:
            list.append(int(input("Digite um valor:")))
            break;
        except:
            trace = traceback.format_exc()
            
            print("Ocorreu um error:", trace)
            
            #vamos criar um arquivo de log do error
            open('trace.log', 'a').write(trace)
            
print(list)