"""
Calculo do segundo digito do CPF
CPF = 449.349.388-77
Colete a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex:  449.349.388-77 (449349388)
   11 10  9  8  7  6  5  4  3  2
*  4   4  9  3  4  9  3  8  8  7 <-- PRIMEIRO DIGITO
   44  40 81 24 28 54 15 32 24 14

Somar todos os resultador:
44+40+81+24+28+54+15+32+24+14 = 356
Multiplicar o resultado por 10
356 * 10 = 3560
Obter o resto da divisão da conta anterior por 11
3560 % 11 = 7
Se o resultado anterior for maior que 9:
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo digito do CPF é 7
"""

cpf = input('Digite seu CPF (apenas números):  ')
dez_digitos = cpf[:10]
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)