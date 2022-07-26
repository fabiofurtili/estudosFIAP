def perguntar():
    return input("O que deseja realizar\n" +
              " I  - Para inserir um novo usuário\n" +
              " P  - Para Pesquisar um usuário\n" +
              " E  - Para Excluir um usuário\n" +
              " L  - Para Listar um usuário\n" +
              "Escolha:  ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite um nome: ").upper(),
                                                   input("Digite uma data: "),
                                                   input("Digite uma estaçao: ").upper()]
    salva(dicionario)

def salva(dicionario):
    with open("db.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor) + "\n")

def excluir(dicionario):
    pass