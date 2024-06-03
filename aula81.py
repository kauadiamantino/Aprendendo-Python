# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


print(perguntas[0]['Pergunta'])
indices = perguntas[0]['Opções']
opcao1 = perguntas[0]['Opções'][0]
opcao2 = perguntas[0]['Opções'][1]
opcao3 = perguntas[0]['Opções'][2]
opcao4 = perguntas[0]['Opções'][3]

for indice, numero in enumerate(indices):
    print(indice, numero)

pergunta1 = input('Escolha uma opção: ')

if pergunta1 == opcao3 :
    print('Você acertou.')
else:
    print('Você errou.')


print(perguntas[1]['Pergunta'])
indices = perguntas[1]['Opções']
opcao1 = perguntas[1]['Opções'][0]
opcao2 = perguntas[1]['Opções'][1]
opcao3 = perguntas[1]['Opções'][2]
opcao4 = perguntas[1]['Opções'][3]

for indice, numero in enumerate(indices):
    print(indice, numero)

pergunta1 = input('Escolha uma opção: ')

if pergunta1 == opcao1 :
    print('Você acertou.')
else:
    print('Você errou.')

print(perguntas[2]['Pergunta'])
indices = perguntas[2]['Opções']
opcao1 = perguntas[2]['Opções'][0]
opcao2 = perguntas[2]['Opções'][1]
opcao3 = perguntas[2]['Opções'][2]
opcao4 = perguntas[2]['Opções'][3]

for indice, numero in enumerate(indices):
    print(indice, numero)

pergunta1 = input('Escolha uma opção: ')

if pergunta1 == opcao2 :
    print('Você acertou.')
else:
    print('Você errou.')



# Resultado do Exercicio

