import PySimpleGUI as sg


class TelaFilme:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

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

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- ATOR ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Ator', "RD1", key='1')],
            [sg.Radio('Alterar Ator', "RD1", key='2')],
            [sg.Radio('Listar Ator', "RD1", key='3')],
            [sg.Radio('Excluir Ator', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)

    def pega_dados_filme(self):
        print("-------DADOS DO FILME-------")
        id = int(input("Informe o ID do Filme: "))
        titulo = input("Informe o Titulo: ")
        ano = int(input("Informe o ano do Filme: "))
        id_diretor = int(input("Informe o nome do Diretor: "))
        return {"id": id, "titulo": titulo, "ano": ano, "id_diretor": id_diretor}
    
    def mostra_filme(self, dados_filme):
        print("\n----- FILME -----")
        print("ID: ", dados_filme["id"])
        print("Título: ", dados_filme["titulo"])
        print("Ano: ", dados_filme["ano"])
        print("Diretor: ", dados_filme["diretor"])
        
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
