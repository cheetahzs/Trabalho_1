class DiretorRepetidoException(Exception):
    def __init__(self, id):
        self.mensagem = "O diretor de id {} já existe"
        super().__init__(self.mensagem.format(id))