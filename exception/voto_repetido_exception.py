class VotoRepetidoException(Exception):
    def __init__(self, membro):
        self.mensagem = "O membro {} já votou nesta categoria"
        super().__init__(self.mensagem.format(membro))