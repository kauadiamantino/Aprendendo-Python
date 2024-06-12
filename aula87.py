# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Luiz',
#     'sobrenome': 'Miranda',
# }
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

dados_pessoa = {
    'idade': 17,
    'altura': 1.75,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, 3, nome='Joana', qLq=123)
mostro_argumentos_nomeados(**pessoas_completa)