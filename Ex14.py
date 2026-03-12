peso = float(input("Digite o peso dos peixes (kg): "))

limite = 50
multa_por_kg = 4

if peso > limite:
    excesso = peso - limite
    multa = excesso * multa_por_kg
else:
    excesso = 0
    multa = 0

print("Excesso de peso:", excesso, "kg")
print("Valor da multa: R$", multa)
