try:
    num = float(input("Digite um número: "))
    print(f"Você digitou o número: {num}")
except ValueError:
    print("Erro: Entrada inválida! Por favor, insira um número.")
