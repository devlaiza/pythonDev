import random

opcoes = ["pedra", "papel", "tesoura"]
jogador_pontos = 0
computador_pontos = 0

print("=== PEDRA, PAPEL E TESOURA ===")

while True:
    jogador = input(
        "\nEscolha pedra, papel, tesoura ou sair: "
    ).strip().lower()

    if jogador == "sair":
        break

    if jogador not in opcoes:
        print("Escolha inválida!")
        continue

    computador = random.choice(opcoes)

    print("Você escolheu:", jogador)
    print("Computador escolheu:", computador)

    if jogador == computador:
        print("Empate!")
    elif (
        (jogador == "pedra" and computador == "tesoura")
        or (jogador == "papel" and computador == "pedra")
        or (jogador == "tesoura" and computador == "papel")
    ):
        print("Você venceu!")
        jogador_pontos += 1
    else:
        print("O computador venceu!")
        computador_pontos += 1

    print(f"Placar: Você {jogador_pontos} x {computador_pontos} Computador")

print("\n=== PLACAR FINAL ===")
print("Jogador:", jogador_pontos)
print("Computador:", computador_pontos)
print("Obrigado por jogar!")
