import random

primeiro = input("primeiro aluno:")
segundo = input("segundo aluno:")
terceiro = input("terceiro aluno:")
quarto = input("quarto aluno:")

lista = [primeiro,segundo,terceiro,quarto]
sorteando = random.choice(lista)

print(f'O aluno sorteado foi {sorteando}')
