''''

    Fatiamento/slice
    Seleciona um pedaço de uma string, lista ou tupla

'''

# seleciono nome
nome = "Leticia Resina"
print(nome)
primeiroNome = nome[0:7] # se eu colocar 6, ele para no i, como o range
print(primeiroNome)
sobrenome = nome[8:15]
print(sobrenome)

# pulando de 2 em 2
exemplo = nome[3:12:2]
print(exemplo)

exemplo2 = nome[2:] # vai pegar do indice 2 ate o final
print(exemplo2)