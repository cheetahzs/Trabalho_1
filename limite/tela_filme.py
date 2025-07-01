import PySimpleGUI as sg


class TelaFilme:
    
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        
        return opcao
    
    def init_opcoes(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text("------- FILMES -------" , font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=('Helvica', 15))],
            [sg.Radio('Incluir Filme', "RD1", key='1')],
            [sg.Radio('Alterar Filme', "RD1", key='2')],
            [sg.Radio('Listar Filme', "RD1", key='3')],
            [sg.Radio('Excluir Filme', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)
    
        
    def pega_dados_filme(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('------- DADOS DO FILME -------', font=("Helvica", 25))],
            [sg.Text('Id do Filme:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Text('Titulo do Filme:', size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Text('Ano do Filme:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Text('Nome do Diretor', size=(15, 1)), sg.InputText('', key='nome_diretor')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)
        
        button, values = self.open()
        id = int(values['id'])
        titulo = values['titulo']
        ano = values['ano']
        nome_diretor = values['nome_diretor']
        
        self.close()
        return {"id": id, "titulo": titulo, "ano": ano, "nome_diretor": nome_diretor}  
    
    def mostra_filme(self, dados_filme):
        string_todos_filmes = ""
        for dado in dados_filme:
            string_todos_filmes = string_todos_filmes + "ID DO FILME: " + str(dado["id"]) + '\n'
            string_todos_filmes = string_todos_filmes + "TITULO DO FILME: " + dado["titulo"] + '\n'
            string_todos_filmes = string_todos_filmes + "ANO DO FILME: " + str(dado["ano"]) + '\n'
            string_todos_filmes = string_todos_filmes + "DIRETOR DO FILME: " + dado["diretor"] + '\n\n'    

        sg.Popup('-------- LISTA DE FILMES ----------', string_todos_filmes)
        
    def seleciona_filme(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('------- SELECIONA FILME -------', font=("Helvica", 25))],
            [sg.Text('Digite o id do filme que deseja selecionar: ', font=("Helvica", 15))],
            [sg.Text('Id: ', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)
        button, values = self.open()
        id = int(values['id'])
        self.close()
        return id
    
    def tela_opcoes_categoria(self):
        self.init_opcoes_categoria()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes_categoria(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- CATEGORIAS DO FILME ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Categoria', "RD1", key='1')],
            [sg.Radio('Alterar Categoria', "RD1", key='2')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)

    def close(self):
        self.__window.Close()
        
    def open(self):
        button, values = self.__window.Read()
        return button, values