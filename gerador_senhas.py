# Passo a passo

# 1 - Montar o conjunto de caracteres permitidos com string
# 2 - Sorteia 1 caractere de cada categoria com secrets.choice, garantindo que tenha maiúscula, minúscula, número e símbolo
# 3 - Completa o tamanho restante sorteando de todos os caracteres
# 4 - Embaralha com SystemRandom().shuffle e junta tudo com "".join(..)

import secrets
import string


# Função: recebe um tamanho e devolve uma senha aleatória, forte e que
# sempre contém os quatro tipos de caractere (minúscula, maiúscula, número e símbolo).
# Ela fica FORA de cadastrar_usuario, para existir sozinha e poder ser chamada de qualquer lugar.
def gerar_senha(tamanho=16):
    minusculas = string.ascii_lowercase
    maiuscula = string.ascii_uppercase
    numero = string.digits
    simbolos = string.punctuation
    todos = minusculas + maiuscula + numero + simbolos

    # Garante que a senha tenha pelo menos um de cada tipo
    senha = [
        secrets.choice(minusculas),
        secrets.choice(maiuscula),
        secrets.choice(numero),
        secrets.choice(simbolos),
    ]

    # Completa o restante com caracteres de qualquer tipo
    for _ in range(tamanho - 4):
        senha.append(secrets.choice(todos))

    # Embaralha para os obrigatórios não ficarem sempre no começo
    secrets.SystemRandom().shuffle(senha)

    return "".join(senha)


def cadastrar_usuario():
    senha_cadastrada = "Python_secrets"
    print("Olá, digite a senha cadastrada para o seu usuário")
    tentativa_cadastro = input("SENHA: ")

    if tentativa_cadastro == senha_cadastrada:
        print("SENHA CORRETA! USUÁRIO CADASTRADO COM SUCESSO")
    else:
        print("SENHA INCORRETA!")
        print("[1] sim [2] não")
        print("  ")
        # input() é o que realmente PERGUNTA e guarda a resposta do usuário
        opcao = input("Gostaria que recomendássemos uma senha segura? ")

        # input() devolve texto, por isso comparamos com "1" (entre aspas)
        if opcao == "1":
            print("Sua senha recomendada é:", gerar_senha(16))
        elif opcao == "2":
            print("Tudo bem, tente novamente mais tarde.")
        else:
            print("Opção inválida. Digite 1 ou 2.")


# Sem esta chamada o programa não faz nada: definir uma função só "ensina" o Python, não executa.
cadastrar_usuario()