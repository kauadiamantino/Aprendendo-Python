# Exercicios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(numero):
#     return numero * 2

# vezes = duplicar(6)

# print(vezes)


# def triplicar(numero):
#     return numero * 3

# vezes = triplicar(6)

# print(vezes)

# def quadruplicar(numero):
#     return numero * 4

# vezes = quadruplicar(6)

# print(vezes)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))