import secrets
import string

def gerar_senha(tamanho):
    if tamanho < 4 or tamanho > 128:
        raise ValueError("O tamanho deve estar entre 4 e 128.")

    letras = string.ascii_letters
    numeros = string.digits
    simbolos = "!@#$%&*+-_?"

    caracteres = letras + numeros + simbolos
    senha = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(numeros),
        secrets.choice(simbolos)
    ]

    senha.extend(
        secrets.choice(caracteres)
        for _ in range(tamanho - 4)
    )

    secrets.SystemRandom().shuffle(senha)

    return "".join(senha)

print("=== GERADOR DE SENHAS ===")

try:
    tamanho = int(input("Tamanho da senha (4 a 128): "))
    senha = gerar_senha(tamanho)

    print("Senha gerada:", senha)

    opcao = input("Gerar outra senha? (s/n): ").strip().lower()

    if opcao == "s":
        tamanho = int(input("Novo tamanho: "))
        print("Nova senha:", gerar_senha(tamanho))

except ValueError as erro:
    print("Entrada inválida:", erro)
