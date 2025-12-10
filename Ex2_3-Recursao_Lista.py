'''
Dada uma lista de n números, implemente uma função recursiva que rtorna o maior elemento do conjunto.
Dada uma lista de n números, implemente uma função recursiva que retorna a soma de todos os elementos do conjunto
'''


def lista(l):
    if len(l) == 1:
        return l[0]
    m = lista(l[1:])
    if l[0] > m:
        return l[0]
    else:
        return m
    
l = lista([1, 5, 10, 20])

print(l)


def listas(l):
    if len(l) == 1:
        return l[0]
    else:
        soma = l[0] + listas(l[1:])
        return soma
    
l = listas([1, 5, 10, 20])

print(l)