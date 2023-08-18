
'''

    TUPLAS

    Sequência de itens, como uma lista, entretanto, a tupla é imutável! Ou seja, não pode ser modificada!
    Não posso inserir, excluir, modificar e afins. Mas posso visualizar valores, acessando ou não pelo indice
    Tuplas = ()
    São heterogêneas (armazena diferentes tipos de dados)

'''

tupla = (3, 2, 10, 5, 2, 2)

tupla2 = (1, 1, 8, 9, 9)

print(tupla)
print(tupla[2])

# index: retorna o indice de um determinado item
print(tupla.index(2))

# count - quantidade de vezes que um item aparece na lista/tupla
print(tupla.count(2))

# in - ver se tem ou não um item
if 8 in tupla:
    print("Existe")
else:
    print("Não existe")

# concatenação de tuplas 
tupla3 = tupla + tupla2
print(tupla3)

# importante! apenas concatena string com string, lista com lista e tupla com tupla!    ]

def teste(a,b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao # sempre que retorno mais de um, o python retorna como tupla

resultado = teste(10, 5)
print(resultado)
print(resultado[0]) # posso pedir pra retornar o indce
print(resultado[1])

# se for somente um elemento dentro de uma tupla, é obrigatório colocar uma , no final
tupla4 = (10,)
print(tupla4)

# list - copia os itens de uma tupla para uma lista => isso não exclui uma a outra
tupla5 = (4, 5, 6)
lista = list(tupla5)
print(lista)

# tuple - copia os itens de uma lista pra uma tupla => isso não exclui uma a outra
lista1 = [1,2,3,4,5]
tupla1 = tuple(lista1)
print(tupla1)

