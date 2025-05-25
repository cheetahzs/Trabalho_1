class telaFilme:
    
    def tela_opcoes(self):
        print("\n ---------- FILMES ----------")
        print("1 - Incluir Filme")
        print("2 - Alterar filme")
        print("3 - Listar Filmes")
        print("4 - Excluir Filme")
        print("5 - Gerenciar Categorias")
        print("0 - Retornar")
        opcao = int(input("Escolha uma opção: "))
        return opcao
    
    def pega_dados_filme(self):
        print("-------DADOS DO FILME-------")
        id = int(input("Informe o ID do Filme: "))
        titulo = input("Informe o Titulo: ")
        ano = int(input("Informe o ano do Filme: "))
        diretor = input("Informe o nome do Diretor: ")