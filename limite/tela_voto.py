class TelaVoto:
    def tela_opcoes(self):
        print("-------- VOTO ----------")
        print("1 - Incluir Voto")
        print("2 - Alterar Voto")
        print("3 - Listar Voto")
        print("4 - Excluir Voto")
        print("5 - Apurar Vencedores")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_voto(self):
        print("-------- DADOS VOTO ----------")
        membro = input("Membro: ")
        categoria = input("Categoria: ")
        alvo = input("Alvo: ")
        return {"membro": membro, "categoria": categoria, "alvo": alvo}

    def mostra_voto(self, dados_voto):
        print("MEMBRO QUE VOTOU: ", dados_voto["membro"])
        print("CATEGORIA: ", dados_voto["categoria"])
        print("ALVO DO VOTO: ", dados_voto["alvo"])

    def seleciona_voto(self):
        membro = input("Membro a ser selecionado: ")
        categoria = input("Categoria a ser selecionado: ")
        return membro, categoria

    def mostra_mensagem(self, msg):
        print(msg)
