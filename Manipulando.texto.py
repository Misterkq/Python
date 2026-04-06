nome = input("Diga seu nome completo:")
letras = nome.split()

print(f"Seu nome com todas letra maiuscula: {nome.upper()}")
print(f"Seu nome com todas letra minuscula: {nome.lower()}")
print(f"Tamanho do seu nome(Não considera o espaço): {len(nome.replace(" ", ""))}")
print(f"Quantas letra tem o primeiro nome: {len(letras[0])}")