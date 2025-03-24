import datetime

def mpe(m):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return meses[m-1]

def vd(data):
    try:
        datetime.datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def de(data):
    if not vd(data):
        return None
    d, m, a = map(int, data.split('/'))
    mn = mpe(m)
    return f"{d} de {mn} de {a}"

data_in = input("Digite a data no formato DD/MM/AAAA: ")
res = de(data_in)

if res:
    print(f"Data no formato extenso: {res}")
else:
    print("Data inválida!")
