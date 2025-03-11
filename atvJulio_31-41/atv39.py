
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(a, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2 if b != 0 else "Erro! Divisão por zero."


n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

operacao = input("Escolha a operação (+, -, *, /): ")


if operacao == "+":
    print("Resultado:", soma(n1, n2))
elif operacao == "-":
    print("Resultado:", subtracao(n1, n2))
elif operacao == "*":
    print("Resultado:", multiplicacao(n1, n2))
elif operacao == "/":
    print("Resultado:", divisao(n1, n2))
else:
    print("Operação inválida!")
