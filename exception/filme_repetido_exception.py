class FilmeRepetidoException(Exception):
    def __init__(self, titulo):
        self.mensagem = "O filme de titulo {} já existe"
        super().__init__(self.mensagem.format(titulo))