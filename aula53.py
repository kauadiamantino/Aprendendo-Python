'''
enumerate - enumera iteráveis (índices)
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('joão')

for indice, nome in enumerate(lista):
    print(indice, nome)

# for indice, nome in enumerate(lista):
#     print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(item)

# for item in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in item:
#         print(f'\t{valor}')