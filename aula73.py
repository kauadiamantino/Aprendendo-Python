"""
Exercicio com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variavel e mostre o valor
da variavel

Crie uma função que fala se um número é par ou impar.
Retorne se o número é par ou ímpar
"""

# Exercicio 1:

# def multiplicar(*args):
#     total = 1
   
#     for numero in args:
#         total *= numero
#     return total


# novo_total = multiplicar(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(novo_total)

# print(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)


# Exercicio 2:

def par_impar(n):
    
    
    if n % 2 == 0:
     return "par"
    
    return "ímpar"
    
numero = int(input("Digite um número: "))
resultado = par_impar(numero)
print(f"O número {numero} é {resultado}.")
