import datetime

data_usuario = input("Digite uma data (dd/mm/aaaa): ")


data = datetime.datetime.strptime(data_usuario, "%d/%m/%Y")


dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
print(f"O dia da semana correspondente é: {dias_da_semana[data.weekday()]}")
