# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser Verdadeiras
# Se qualquer valor for consideirado falso,
# a expressão inteiras será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo none que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')

senha_permitida = '123456'



if entrada == 'E' and senha == senha_permitida:
    print('Entrar')

else:
    print('Sair')