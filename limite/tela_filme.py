class TelaFilme:
    
    def tela_opcoes(self):
        print("\n------- FILMES -------")
        print("1 - Incluir Filme")
        print("2 - Alterar Filme")
        print("3 - Listar Filme")
        print("4 - Excluir Filme")
        print("0 - Retornar")
        
        opcao = int(input("Escolha uma opção: "))
        return opcao
    
    def pega_dados_filme(self):
        print("------- DADOS DO FILME -------")
        id = input("Id do filme: ")
        titulo = input("Titulo do filme: ")
        ano = input("Ano do filme: ")
        nome_diretor = input("Nome do Diretor: ")
        return {"id": id, "titulo": titulo, "ano": ano, "nome_diretor": nome_diretor}
    
    def mostra_filme(self, dados_filme):
        print("\n------- LISTA DE FILMES -------")
        print("ID DO FILME", dados_filme["id"])
        print("TITULO DO FILME", dados_filme["titulo"])
        print("NOME DO DIRETOR", dados_filme["nome_diretor"])
        print("ANO DO FILME", dados_filme["ano"])

    
    def seleciona_filme(self):
        filme = input("Id do filme a ser selecionado: ")
        return filme
    
    def mostra_mensagem(self, msg):
        print(msg)