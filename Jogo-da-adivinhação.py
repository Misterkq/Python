import random

print("=" * 30)
print("jogo da adivinhação| adivinhar um numero de 1 a 10")
print("=" * 30)

recorde = 0

try:
    while True:
        print("[1]jogar" \
              "[2]ver recorde" \
              "[3] sair")

        opc = input("escolha uma das opção:")
        match opc:
            case "1":
                numero_secreto = random.randint(1,10)
                adivinhar = int(input("faça seu palpite:"))
                if numero_secreto == adivinhar:
                    print("Voce acertou! +10 pontos")
                    recorde += 10
                else:
                    print("voce errou! -10 pontos")
                    recorde = max(0, recorde -10)
            
            case "2":
                print(f"seu record atual é {recorde}!")

            case"3":
                print("saindo")
                break

except ValueError:
    print("apenas digitar numero!")




