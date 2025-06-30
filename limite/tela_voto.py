import PySimpleGUI as sg


class TelaVoto:
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
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- VOTO ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Voto', "RD1", key='1')],
            [sg.Radio('Alterar Voto', "RD1", key='2')],
            [sg.Radio('Listar Voto', "RD1", key='3')],
            [sg.Radio('Excluir Voto', "RD1", key='4')],
            [sg.Radio('Apurar Vencedores', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)

    def pega_dados_voto(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- NOVO VOTO ----------', font=("Helvica", 25))],
            [sg.Text('ID do membro:', size=(20, 1)), sg.InputText('', key='membro_id')],
            [sg.Text('Nome da categoria:', size=(20, 1)), sg.InputText('', key='categoria')],
            [sg.Text('ID do alvo:', size=(20, 1)), sg.InputText('', key='alvo_id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Sistema de Votação do Oscar').Layout(layout)
        button, values = window.Read()
        window.Close()

        # Conversão e validação
        try:
            membro_id = int(values['membro_id'])
            alvo_id = int(values['alvo_id'])
            categoria = values['categoria'].strip()
        except (ValueError, TypeError):
            sg.popup("Erro: Informe valores válidos.")
            return self.pega_dados_voto()

        return {
            "membro_id": membro_id,
            "categoria": categoria,
            "alvo_id": alvo_id
        }

    def mostra_voto(self, dados_voto):
        string_todos_votos = ""
        for dado in dados_voto:
            string_todos_votos = string_todos_votos + "MEMBRO QUE VOTOU: " + dado["membro"] + '\n'
            string_todos_votos = string_todos_votos + "CATEGORIA: " + dado["categoria"] + '\n'
            string_todos_votos = string_todos_votos + "ALVO DO VOTO: " + dado["alvo"] + '\n\n'
            

        sg.Popup('-------- LISTA DE VOTOS ----------', string_todos_votos)

    def seleciona_voto(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONA VOTO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o membro e categoria do voto que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Membro: ', size=(15, 1)), sg.InputText('', key='membro')],
            [sg.Text('Categoria: ', size=(15, 1)), sg.InputText('', key='categoria')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação do Oscar').Layout(layout)

        button, values = self.open()
        membro = values['membro']
        categoria = values['categoria']
        self.close()
        return membro, categoria

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
