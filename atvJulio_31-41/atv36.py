

def ler_matriz():
    matriz = []
    for i in range(12):
        linha = list(map(int, input(f"Digite os 13 elementos da linha {i+1}: ").split()))
        matriz.append(linha)
    return matriz

def modificar_matriz(matriz):
    for i in range(12):
        maior_elemento = max(matriz[i]) 
        matriz[i] = [x / maior_elemento for x in matriz[i]] 
    return matriz


def main():

    A = ler_matriz()
    

    A_modificada = modificar_matriz(A)
    
 
    print("\nMatriz A modificada:")
    for linha in A_modificada:
        print([f"{x:.1f}" for x in linha])  


main()
