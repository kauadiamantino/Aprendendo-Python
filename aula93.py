# dir, hasattr e getattr em Python
string = 'kaua'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string)