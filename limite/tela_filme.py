from controlador.controlador_filme import ControladorFilme

class TelaFilme:
    
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
        id_diretor = int(input("Informe o nome do Diretor: "))
        return {"id": id, "titulo": titulo, "ano": ano, "id_diretor": id_diretor}
    
    def mostra_filme(self, dados_filme):
        print("\n----- FILME -----")
        print(f"ID: {dados_filme["id"]}")
        print(f"Título: {dados_filme["titulo"]}")
        print(f"Ano: {dados_filme["ano"]}")
        print(f"Diretor: {dados_filme["diretor"]}")
        
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")
        
    def seleciona_filme(self):
        id = int(input("\nDigite o ID do Filme: "))
        return id
    
    def tela_opcoes_categoria(self):
        print("\n----- CATEGORIAS DO FILME -----")
        print("\n1 - Adicionar Categoria")
        print("\n2 - Remover Categoria")
        opcao = int(input("Escolha uma opção: "))
        return opcao
    
    def pega_nome_categoria(self):
        nome = input("Nome da categoria a remover")
        return nome