def div(a, b):
    return a / b

def vm(d, t):
    return div(d, t)

d = float(input("Distância (km): "))
t = float(input("Tempo (h): "))

v = vm(d, t)

print(f"Velocidade média: {v} km/h")
