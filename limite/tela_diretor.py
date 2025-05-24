class TelaDiretor:
    def tela_opcoes(self):
        print("-------- DIRETOR ----------")
        print("1 - Incluir Diretor")
        print("2 - Alterar Diretor")
        print("3 - Listar Diretor")
        print("4 - Excluir Diretor")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def pega_dados_diretor(self):
        print("-------- DADOS DIRETOR ----------")
        id = input("Id: ")
        nome = input("Nome: ")
        data_de_nascimento = input("Data de Nascimento: ")
        nacionalidade = input("Nacionalidade: ")
        return {"id": id, "nome": nome, "data_de_nascimento": data_de_nascimento,
                 "nacionalidade": nacionalidade}
    
    def mostra_diretor(self, dados_diretor):
        print("ID DO DIRETOR", dados_diretor["id"])
        print("NOME DO DIRETOR: ", dados_diretor["nome"])
        print("DATA DE NASCIMENTO DO DIRETOR", dados_diretor["data_de_nascimento"])
        print("NACIONALIDADE DO DIRETOR", dados_diretor["nacionalidade"])
        

    def seleciona_diretor(self):
        diretor = input("Id do diretor a ser selecionado: ")
        return diretor
    
    def mostra_mensagem(self, msg):
        print(msg)
