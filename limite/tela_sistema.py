class TelaSistema:
    
    def tela_opcoes(self):
        print("\n===== MENU PRINCIPAL =====")
        print("\nEscolha sua opção")
        print("1 - Gerenciar Atores")
        print("2 - Gerenciar Categorias")
        print("3 - Gerenciar Diretores")
        print("4 - Gerenciar Filmes")
        print("5 - Votação")
        print("0 - Encerrar sistema")
        try:
            return int(input("Escolha uma opção"))
        except ValueError:
            return -1
        
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")