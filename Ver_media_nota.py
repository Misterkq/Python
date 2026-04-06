guarda = []

while len(guarda) < 2:
    nota = float(input("Diga sua nota: "))
    if nota > 10 or nota < 1:
        print("Apenas notas de 1 a 10")
    else:
        guarda.append(nota)

media = (guarda[0] + guarda[1]) / 2
print(media)
