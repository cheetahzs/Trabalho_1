from limite.tela_filme import TelaFilme
from entidade.filme import Filme


class ControladorFilme:
    def __init__(self, controlador_sistema):
        self.__filmes = []
        self.__telaFilme()
        self.__controlador_sistema = controlador_sistema

    def pega_filme_por_id(self, id_filme):
        for filme in self.__filmes:
            if filme.id == id_filme:
                return filme
        return None
