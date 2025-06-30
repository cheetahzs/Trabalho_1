class FilmeRepetidoException(Exception):
    
    def __init__(self, id):
        self.mensagem = "O filme de id {} já existe."
        super().__init__(self.mensagem.format(id))