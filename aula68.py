"""
Argumentos nomeados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} {z=}', '|', 'x + y = ', x + y + z)

soma(1, 2, 6)
soma(2, 1, 6)
soma(y=2, x=1, z=6)
soma(9, z=6, y=1)