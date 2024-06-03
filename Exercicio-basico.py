altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print(
        'Seu IMC é ' , imc,'.' 'Você está abaixo do peso.'
        )
elif imc <= 24.9:
    print(
        'Seu IMC é ' , imc,'.' 'Você está com peso ideal'
        )
elif imc <= 29.9:
    print(
        'Seu IMC é ' , imc,'.' 'Você está com sobrepeso'
        )
else:
    print(
        'Seu IMC é ', imc,'.' 'Você está com obesidade'
        )


# peso = float(input("Digite seu peso (em kg): "))
# altura = float(input("Digite sua altura (em metros): "))

# imc = peso / (altura * altura)

# if imc < 18.5:
#     classificacao = "Abaixo do peso"
# elif imc < 25:
#     classificacao = "Peso normal"
# elif imc < 30:
#     classificacao = "Sobrepeso"
# else:
#     classificacao = "Obesidade"

# print(f"Seu IMC é: {imc:.2f}")
# print(f"Classificação: {classificacao}")
