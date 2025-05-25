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