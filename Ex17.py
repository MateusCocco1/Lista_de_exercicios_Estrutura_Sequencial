area = float(input("Digite a área em m²: "))

area = area * 1.10
litros = area / 6

latas = litros / 18
latas = int(latas)
if litros % 18 != 0:
    latas = latas + 1
preco_latas = latas * 80

galoes = litros / 3.6
galoes = int(galoes)
if litros % 3.6 != 0:
    galoes = galoes + 1
preco_galoes = galoes * 25

# mistura
latas_m = int(litros / 18)
resto = litros - (latas_m * 18)

galoes_m = int(resto / 3.6)
if resto % 3.6 != 0:
    galoes_m = galoes_m + 1

preco_misto = latas_m * 80 + galoes_m * 25

melhor_preco = preco_latas
tipo = "apenas latas"

if preco_galoes < melhor_preco:
    melhor_preco = preco_galoes
    tipo = "apenas galoes"

if preco_misto < melhor_preco:
    melhor_preco = preco_misto
    tipo = "mistura de latas e galoes"

print("Melhor opcao:", tipo)
print("Preco: R$", melhor_preco)
