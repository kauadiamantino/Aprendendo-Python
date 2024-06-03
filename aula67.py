def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)


# import json

# def carregar_lista():
#     try:
#         with open("lista_compras.json", "r") as arquivo:
#             return json.load(arquivo)
#     except FileNotFoundError:
#         return []

# def salvar_lista(lista_compras):
#     with open("lista_compras.json", "w") as arquivo:
#         json.dump(lista_compras, arquivo, indent=4)

# def adicionar_item():
#     item = input("Digite o item a ser adicionado: ")
#     lista_compras.append(item)
#     salvar_lista(lista_compras)
#     print(f"'{item}' adicionado à lista de compras.")

# def remover_item():
#     if not lista_compras:
#         print("A lista de compras está vazia.")
#         return

#     index = int(input("Digite o índice do item a ser removido: "))
#     try:
#         item_removido = lista_compras.pop(index)
#         salvar_lista(lista_compras)
#         print(f"'{item_removido}' removido da lista de compras.")
#     except IndexError:
#         print("Índice inválido.")

# def listar_itens():
#     if not lista_compras:
#         print("A lista de compras está vazia.")
#     else:
#         print("Lista de compras:")
#         for i, item in enumerate(lista_compras):
#             print(f"{i}: {item}")

# lista_compras = carregar_lista()

# while True:
#     print("\nOpções:")
#     print("1 - Adicionar item")
#     print("2 - Remover item")
#     print("3 - Listar itens")
#     print("4 - Sair")

#     escolha = input("Escolha uma opção: ")

#     if escolha == "1":
#         adicionar_item()
#     elif escolha == "2":
#         remover_item()
#     elif escolha == "3":
#         listar_itens()
#     elif escolha == "4":
#         break
#     else:
#         print("Opção inválida.")