'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer depois dos zeros
Sinal - + ou -
Ex.: 0>-100, .1f
Conversion flags - !r !s !a
'''
variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:=<10}.')
print(f'{variavel:o^10}.')
print(f'{1000.123485165106484:,.2f}')
print(f'{1000.123485165106484:0=+10,.2f}')
print(f'{1000.123485165106484:,.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')