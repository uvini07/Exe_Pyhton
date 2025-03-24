try:
    num = int(input("Digite um número inteiro: "))
    print(f"O quadrado de {num} é {num ** 2}")
except ValueError:
    print("Erro: Entrada inválida! Por favor, insira um número inteiro.")
