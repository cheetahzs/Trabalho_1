from membro_academia import MembroAcademia


class Diretor(MembroAcademia):
    def __init__(self, id: int, nome: str,
                 data_nascimento: str, nacionalidade: str):
        super().__init__(id, nome, data_nascimento, nacionalidade)
