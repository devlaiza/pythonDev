alunos = []

def cadastrar_aluno():
    nome = input("Nome do aluno: ")

    try:
        nota1 = float(input("Primeira nota: "))
        nota2 = float(input("Segunda nota: "))

        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            print("As notas devem estar entre 0 e 10.")
            return

        media = (nota1 + nota2) / 2

        aluno = {
            "nome": nome,
            "media": media
        }

        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    except ValueError:
        print("Digite notas válidas!")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        situacao = "Aprovado" if aluno["media"] >= 7 else "Reprovado"
        print(
            f'{aluno["nome"]} | '
            f'Média: {aluno["media"]:.1f} | {situacao}'
        )

while True:
    print("\n=== SISTEMA DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
