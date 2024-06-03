valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

primeiro_valor = f'{valor1} é maior ou igual ao segundo valor {valor2} '
segundo_valor = f'{valor2} é maior ou igual ao primeiro valor {valor1}'


if valor1 >= valor2:
    print(primeiro_valor)

else:
    print(segundo_valor)