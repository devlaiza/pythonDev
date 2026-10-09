def calculadora():
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    while True:
        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Calculadora encerrada!")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida!")
            continue

        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = n1 + n2
            elif opcao == "2":
                resultado = n1 - n2
            elif opcao == "3":
                resultado = n1 * n2
            else:
                if n2 == 0:
                    print("Não é possível dividir por zero!")
                    continue
                resultado = n1 / n2

            print("Resultado:", resultado)

        except ValueError:
            print("Digite números válidos!")


calculadora()
