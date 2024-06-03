'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
numero = input ('Vou dobrar o número que você digitar: ')

try:
    print('STR:', numero)
    numero_float = float(numero)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2:.0f}')
except:
    print('Isso não é um número')    
'''print(numero.isdigit())
if numero.isdigit():
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2:.0f}')
else:
    print('Isso não é um número')
'''
