tamanho = float(input("Digite o tamanho do arquivo (MB): "))
velocidade = float(input("Digite a velocidade da internet (Mbps): "))

tempo = tamanho / velocidade

print("Tempo aproximado de download:", tempo, "segundos")
