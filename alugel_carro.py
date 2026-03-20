dias = float(input("Quantos dias alugado? "))
km = float(input("Quanto Km rodado? "))
custo_dia = dias * 60
custo_km = km * 0.15
valor_total = custo_dia + custo_km
print(f"O total a pagar é de R${valor_total}")
