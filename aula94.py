import sys

# Generator expression, Iterables e Iteradores em Python
iterable = ['Eu', 'Tenho', '_iter_']
iterator = iter(iterable) # tem _iter_ e _next_
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
lista = [n for n in range(100000000)]
generator = (n for n in range(100000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)


#for n in generator:
#    print(n)