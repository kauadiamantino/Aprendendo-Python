'''
Introdução às funções (def) em Python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
'''


# def imprimir(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# imprimir(1,2,3)

def saudacao(nome= 'Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Kauã')
saudacao('Luiz')
saudacao('Rafa')
saudacao()