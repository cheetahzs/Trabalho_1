from limite.tela_filme import TelaFilme
from entidade.filme import Filme
from controlador_diretor import ControladorDiretor


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
<<<<<<< HEAD
    
    def incluir_filme(self):
        dados = self.__tela.filme.pega_dados_filme()
        if self.pega_filme_por_id(dados[id]) is None:
            diretor = self.__controlador_sistema.pega_diretor_por_id(dados["id_diretor"])
            novo_filme = Filme(
                id = dados["id"],
                titulo = dados["titulo"],
                diretor = diretor,
                ano = dados["ano"],
                categorias = []
            )
            self.__filmes.append(novo_filme)
        else:
            self.__tela_filme.mostra_mensagem("Filme já existente com esse ID.")
=======
>>>>>>> 0a3bf2f912fe4dd8a9c7ead8adcafe7645c1591d
            
    def alterar_filme(self):
        self.lista_filmes()
        id_filme = self.__tela_filme.seleciona_filme()