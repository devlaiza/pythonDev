import json
from pathlib import Path

ARQUIVO = Path("tarefas.json")

def carregar():
    if ARQUIVO.exists():
        try:
            return json.loads(ARQUIVO.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Erro ao carregar tarefas.")
    return []

def salvar():
    ARQUIVO.write_text(
        json.dumps(tarefas, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )

tarefas = carregar()

while True:
    print("\n=== LISTA DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        descricao = input("Nova tarefa: ").strip()

        if descricao:
            tarefas.append({
                "descricao": descricao,
                "concluida": False
            })
            salvar()
            print("Tarefa adicionada!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")

        for i, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f'{i} - {tarefa["descricao"]} [{status}]')

    elif opcao in ("3", "4"):
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i} - {tarefa["descricao"]}')

        try:
            numero = int(input("Número da tarefa: "))

            if not 1 <= numero <= len(tarefas):
                print("Número inválido!")
                continue

            if opcao == "3":
                tarefas[numero - 1]["concluida"] = True
                print("Tarefa concluída!")
            else:
                tarefas.pop(numero - 1)
                print("Tarefa excluída!")

            salvar()

        except ValueError:
            print("Digite um número válido.")

    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
