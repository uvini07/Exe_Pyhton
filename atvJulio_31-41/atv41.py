def velocidade_media(distancia, tempo):
    if tempo != 0:
        return distancia / tempo
    else:
        return "Erro! Tempo não pode ser zero."

distancia = float(input("Distância percorrida (em metros): "))
tempo = float(input("Tempo gasto (em segundos): "))

resultado = velocidade_media(distancia, tempo)

if isinstance(resultado, str):
    print(resultado)
else:
    print(f"Velocidade média: {resultado} metros por segundo.")
