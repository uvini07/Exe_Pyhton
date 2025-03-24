def conversao_24_para_12(hora, minuto):
    if hora == 0:
        return f"12:{minuto:02d} A.M."
    elif hora == 12:
        return f"12:{minuto:02d} P.M."
    elif hora > 12:
        return f"{hora - 12}:{minuto:02d} P.M."
    else:
        return f"{hora}:{minuto:02d} A.M."

def mostrar_resultado():
    hora_24 = int(input("Digite a hora (formato 24 horas): "))
    minuto = int(input("Digite os minutos: "))
    resultado = conversao_24_para_12(hora_24, minuto)
    print(f"Hora convertida: {resultado}")

def main():
    while True:
        mostrar_resultado()
        repetir = input("Deseja converter outra hora? (S/N): ").strip().lower()
        if repetir != 's':
            print("Programa encerrado.")
            break

main()
