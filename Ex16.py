area = float(input("Digite o tamanho da área a ser pintada (m²): "))

litros = area / 3
latas = (litros / 18)
preco = latas * 80

print("Quantidade de latas:", latas)
print("Preço total: R$", preco)
