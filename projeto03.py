import json
from pathlib import Path

ARQUIVO = Path("financas.json")

def carregar():
    if ARQUIVO.exists():
        try:
            return json.loads(ARQUIVO.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Não foi possível ler o arquivo.")
    return []

def salvar():
    ARQUIVO.write_text(
        json.dumps(lancamentos, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )

lancamentos = carregar()

while True:
    print("\n=== CONTROLE FINANCEIRO ===")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Ver extrato")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao in ("1", "2"):
        descricao = input("Descrição: ")

        try:
            valor = float(input("Valor em reais: ").replace(",", "."))

            if valor <= 0:
                print("O valor deve ser positivo.")
                continue

            tipo = "receita" if opcao == "1" else "despesa"

            lancamentos.append({
                "descricao": descricao,
                "valor": valor,
                "tipo": tipo
            })

            salvar()
            print("Lançamento salvo!")

        except ValueError:
            print("Digite um valor válido.")

    elif opcao == "3":
        receitas = sum(
            x["valor"] for x in lancamentos
            if x["tipo"] == "receita"
        )
        despesas = sum(
            x["valor"] for x in lancamentos
            if x["tipo"] == "despesa"
        )

        for item in lancamentos:
            print(
                f'{item["tipo"].capitalize()}: '
                f'{item["descricao"]} - R$ {item["valor"]:.2f}'
            )

        print(f"Total de receitas: R$ {receitas:.2f}")
        print(f"Total de despesas: R$ {despesas:.2f}")
        print(f"Saldo: R$ {receitas - despesas:.2f}")

    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
