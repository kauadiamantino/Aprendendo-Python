"""
Calculo do primeiro digito do CPF
CPF: 449.349.388-77
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex:  449.349.388-77 (449349388)
   10 9  8  7  6  5  4  3  2
*  4  4  9  3  4  9  3  8  8
   40 36 72 21 24 45 12 24 16

   Somar todos os resultados:
   40+36+72+21+24+45+12+24+16 = 290
   Multiplicar o resultador anterior por 10 
   290 * 10 = 2900
   obter o resto da divisão da conta anterior por 11
   2900 % 11 = 7
   Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro digito do CPF é 7
"""

cpf = input('Digite seu CPF (apenas números):  ')
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
