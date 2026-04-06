from math import radians,sin,cos,tan

num = float(input("Digite o angulo que voce deseja: "))
transforma = radians(num)

seno = sin(transforma)
cosseno = cos(transforma)
tangente = tan(transforma)

print(f'O angulo de {num} tem o SENO de {seno:.2f}\nO angulo de {num} tem o COSSENO de {cosseno:.2f}\no angulo de {num} tem a TANGENTE de {tangente:.2f}')