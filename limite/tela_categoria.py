import PySimpleGUI as sg


class TelaCategoria:
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
            [sg.Text('-------- CATEGORIAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Categoria', "RD1", key='1')],
            [sg.Radio('Alterar Categoria', "RD1", key='2')],
            [sg.Radio('Listar Categoria', "RD1", key='3')],
            [sg.Radio('Excluir Categoria', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)



    def pega_dados_categoria(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- DADOS CATEGORIA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)

        button, values = self.open()
        nome = values['nome']

        self.close()
        return {"nome": nome}


    def mostra_categoria(self, dados_categoria):
        string_todas_categorias = ""
        for dado in dados_categoria:
            string_todas_categorias = string_todas_categorias + "NOME DA CATEGORIA: " + dado["nome"] + '\n\n'    

        sg.Popup('-------- LISTA DE CATEGORIAS ----------', string_todas_categorias)

    def seleciona_categoria(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONA CATEGORIA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o nome da categoria que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)

        button, values = self.open()
        nome = int(values['nome'])
        self.close()
        return nome


    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
