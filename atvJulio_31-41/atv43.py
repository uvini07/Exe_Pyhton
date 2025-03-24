def organizar_numero(n):
    n_str = str(n)
    crescente = ''.join(sorted(n_str))
    decrescente = ''.join(sorted(n_str, reverse=True))
    reverso = n_str[::-1]
    
    return crescente, decrescente, reverso

n = int(input("Digite um número: "))

c, d, r = organizar_numero(n)

print(f"Crescente: {c}")
print(f"Decrescente: {d}")
print(f"Reverso: {r}")
