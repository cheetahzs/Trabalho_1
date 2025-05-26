class AtorRepetidoException(Exception):
    def __init__(self, id):
        self.mensagem = "O ator de id {} já existe"
        super().__init__(self.mensagem.format(id))