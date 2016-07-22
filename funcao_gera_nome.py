Olá pessoal, hoje estarei montando um exemplo bem legal de como trabalhar com manipulação de string.

Vamos começar criando uma variavel:

>>> nome = 'Fulano Silva'

Digamos que eu preciso pegar os quatros primeiros caracteres do nome seguido do espaço, e os quatros últimos caracteres.

Bem, pra quem já conhece podemos usar o operador slice para podermos extrair as partes que queremos.

>>> primeira_parte = nome[0:4]
>>> primeira_parte
'Fula'
>>> segunda_parte = nome[7:11]
>>> segunda_parte
'Silv'

E agora vamos imprimir o resultado concatenando as variáveis.

>>> print "%s %s" % (primeira_parte, segunda_parte)
'Fula Silv'

Agora pessoal vamos ver um detalhe.

E se o nome tivesse mais uma string?

>>> nome = 'Fulano Silva Cavalcanti'

>>> primeira_parte = nome[0:4]

>>> primeira_parte
'Fula'

>>> segunda_parte = nome[7:11]

>>> segunda_parte
'Silv'

>>> print "%s %s" % (primeira_parte, segunda_parte)
'Fula Silv'

O resultado final é o que esperamos? Não.

Vamos modificar esse codigo e tornar ele mais adaptável em qualquer situação, ou seja, tornar ele um código 'genérico'.

Vou pegar o tamanho da string e ajustar o slice do final da segunda parte com base nesse valor.

E para descobrir o tamanho da string vamos usar a função len.

>>> nome = 'Fulano Silva Cavalcanti'

>>> tamanho = len(nome)

>>> primeira_parte = nome[0:4]

>>> segunda_parte = nome[tamanho-4:tamanho]

>>> print "%s %s" % (primeira_parte, segunda_parte)
'Fula anti'

Bem, valeu pessoal espero que tenham gostado.

Acessem o meu perfil no github e baixem todos os scripts.

https://github.com/sandrocnrj/python_para_todos

Valeu galera um forte abraço para todos.
