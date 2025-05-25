class TelaAtor:
    def tela_opcoes(self):
        print("-------- ATOR ----------")
        print("1 - Incluir Ator")
        print("2 - Alterar Ator")
        print("3 - Listar Ator")
        print("4 - Excluir Ator")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_ator(self):
        print("-------- DADOS ATOR ----------")
        id = input("Id: ")
        nome = input("Nome: ")
        data_de_nascimento = input("Data de Nascimento: ")
        nacionalidade = input("Nacionalidade: ")
        return {"id": id, "nome": nome, "data_de_nascimento": data_de_nascimento,
                 "nacionalidade": nacionalidade}

    def mostra_ator(self, dados_ator):
        print("ID DO ATOR", dados_ator["id"])
        print("NOME DO ATOR: ", dados_ator["nome"])
        print("DATA DE NASCIMENTO DO ATOR", dados_ator["data_de_nascimento"])
        print("NACIONALIDADE DO ATOR", dados_ator["nacionalidade"])

    def seleciona_ator(self):
        ator = input("Id do ator a ser selecionado: ")
        return ator

    def mostra_mensagem(self, msg):
        print(msg)
