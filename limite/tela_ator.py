import PySimpleGUI as sg


class TelaAtor:
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

    def pega_dados_ator(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- DADOS ATOR ----------', font=("Helvica", 25))],
            [sg.Text('Id:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText('', key='data_de_nascimento')],
            [sg.Text('Nacionalidade:', size=(15, 1)), sg.InputText('', key='nacionalidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)

        button, values = self.open()
        id = int(values['id'])
        nome = values['nome']
        data_de_nascimento = values['data_de_nascimento']
        nacionalidade = values['nacionalidade']

        self.close()
        return {"id": id, "nome": nome, "data_de_nascimento": data_de_nascimento,
                "nacionalidade": nacionalidade}

    def mostra_ator(self, dados_ator):
        string_todos_atores = ""
        for dado in dados_ator:
            string_todos_atores = string_todos_atores + "ID DO ATOR: " + str(dado["id"]) + '\n'
            string_todos_atores = string_todos_atores + "NOME DO ATOR: " + dado["nome"] + '\n'
            string_todos_atores = string_todos_atores + "DATA DE NASCIMENTO DO ATOR: " + str(dado["data_de_nascimento"]) + '\n'
            string_todos_atores = string_todos_atores + "NACIONALIDADE DO ATOR: " + dado["nacionalidade"] + '\n\n'    

        sg.Popup('-------- LISTA DE ATORES ----------', string_todos_atores)

    def seleciona_ator(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONA ATOR ----------', font=("Helvica", 25))],
            [sg.Text('Digite o id do ator que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Id:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)

        button, values = self.open()
        id = int(values['id'])
        self.close()
        return id

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
