from random import shuffle

primeiro = input("primeiro aluno:")
segundo = input("segundo aluno:")
terceiro = input("terceiro aluno:")
quarto = input("quarto aluno:")


lista = [primeiro,segundo,terceiro,quarto]
ordem = shuffle(lista)

print(f'A ordem de apresentação dos alunos é: {lista}')
