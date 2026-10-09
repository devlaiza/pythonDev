import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
""")
conexao.commit()

def cadastrar():
    nome = input("Nome do produto: ").strip()

    try:
        preco = float(input("Preço: ").replace(",", "."))
        quantidade = int(input("Quantidade: "))

        if not nome or preco < 0 or quantidade < 0:
            print("Dados inválidos!")
            return

        cursor.execute(
            "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
            (nome, preco, quantidade)
        )
        conexao.commit()
        print("Produto cadastrado!")

    except ValueError:
        print("Preço ou quantidade inválidos.")
    except sqlite3.IntegrityError:
        print("Já existe um produto com esse nome.")

def listar():
    cursor.execute("SELECT * FROM produtos ORDER BY nome")
    produtos = cursor.fetchall()

    if not produtos:
        print("Estoque vazio.")

    for p in produtos:
        alerta = " - ESTOQUE BAIXO" if p[3] < 5 else ""
        print(
            f"ID: {p[0]} | {p[1]} | "
            f"R$ {p[2]:.2f} | Quantidade: {p[3]}{alerta}"
        )

def movimentar():
    listar()

    try:
        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade a adicionar ou retirar: "))

        if quantidade == 0:
            print("Informe uma quantidade diferente de zero.")
            return

        cursor.execute(
            "SELECT quantidade FROM produtos WHERE id = ?",
            (produto_id,)
        )
        produto = cursor.fetchone()

        if produto is None:
            print("Produto não encontrado.")
            return

        nova_quantidade = produto[0] + quantidade

        if nova_quantidade < 0:
            print("Estoque insuficiente!")
            return

        cursor.execute(
            "UPDATE produtos SET quantidade = ? WHERE id = ?",
            (nova_quantidade, produto_id)
        )
        conexao.commit()
        print("Estoque atualizado!")

    except ValueError:
        print("Digite números válidos.")

while True:
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Movimentar estoque (+ entrada, - saída)")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        movimentar()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

conexao.close()
