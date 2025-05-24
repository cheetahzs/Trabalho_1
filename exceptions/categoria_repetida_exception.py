class CategoriaRepetidaException(Exception):
    def __init__(self, nome):
        self.mensagem = "A categoria {} já existe"
        super().__init__(self.mensagem.format(nome))