"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('joão')
indices = range (len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))