largura = float(input("Largura da parede:"))
altura = float(input("Altura da parede:"))

area = largura * altura

litros_tinta = area / 2

print(f"Sua parede tem a dimensão {largura}X{altura} e sua area é {area} \nPara pintar essa parede , voce precisara {litros_tinta}L de tinta")
