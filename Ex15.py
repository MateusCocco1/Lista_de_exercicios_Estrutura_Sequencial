valor_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sindicato

print("Salário Bruto: R$", salario_bruto)
print("Desconto IR (11%): R$", ir)
print("Desconto INSS (8%): R$", inss)
print("Desconto Sindicato (5%): R$", sindicato)
print("Salário Líquido: R$", salario_liquido)
