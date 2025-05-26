from limite.tela_filme import TelaFilme
from entidade.filme import Filme

class ControladorFilme:
    
    def __init__(self, controlador_sistema):
        self.__filmes = []
        self.__tela_filme = TelaFilme()
        self.__controlador_sistema = controlador_sistema

    def pega_filme_por_id(self, id_filme):
        for filme in self.__filmes:
            if filme.id == id_filme:
                return filme
        return None
    
    def incluir_filme(self):
        dados = self.__tela_filme.pega_dados_filme()
        if self.pega_filme_por_id(dados["id"]) is None:
            diretor = self.__controlador_sistema.pega_diretor(dados["id_diretor"])
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
            
    def lista_filmes(self):
        if not self.__filmes:
            self.__tela.filme.mostra_mensagem("Nenhum filme cadastrado.")
        for filme in self.__filmes:
            self.__tela_filme.mostra_filme({
            "id": filme.id,
            "titulo": filme.titulo,
            "ano": filme.ano,
            "diretor": filme.diretor.nome
                })
            
    def exclui_filme(self):
        self.lista_filmes()
        id_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme_por_id(id_filme)
        if filme:
            self.__filmes.remove(filme)
            self.__tela.filme.mostra_mensagem("Filme removido com sucesso.")
        else:
            self.__tela_filme.mostra_mensagem("Filme não encontrado.")