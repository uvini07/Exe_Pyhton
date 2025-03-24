try:
    num = float(input("Digite um número: "))
    resultado = 100 / num
    print(f"Resultado da divisão: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Você deve inserir um número válido!")
