import time
n1 = input("Informe um numero:")
print(f"Analisando o numero {n1}")
time.sleep(1)
u = n1 // 1 % 10
d =  n1 // 10 % 10
c =  n1 // 100 % 10
m = n1 // 100 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')