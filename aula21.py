'''
Operadores in e not in
Strings são iteráveis
0 1 2 3 4 5 
o t á v i o
-6-5-4-3-2-1
'''

#nome = 'Otávio'

#print(nome[1])
#print(nome[2])
#print(nome[3])
#print(nome[4])
#print(nome[5])
#print(10 * '-')
#print ('á' in nome)
#print ('z' in nome)
#print ('O' not in nome)


nome = input('Digite seu nome: ')
encontrar = input('Oque você deseja encontrar? ')

if encontrar in nome:
    print(f'{encontrar} entá em {nome}')
else:
    print(f'{encontrar} não entá em {nome}')