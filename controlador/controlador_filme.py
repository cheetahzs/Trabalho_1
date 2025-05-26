from limite.tela_filme import TelaFilme
from entidade.filme import Filme

class ControladorFilme:
    
    def __init__(self, controlador_sistema):
        self.__filmes = []
        self.__tela_filme = TelaFilme()
        self.__controlador_sistema = controlador_sistema

    def pega_filme(self, id_filme):
        for filme in self.__filmes:
            if filme.id == id_filme:
                return filme
        return None
    
    def incluir_filme(self):
        dados = self.__tela_filme.pega_dados_filme()
        if self.pega_filme(dados["id"]) is None:
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
            
    def alterar_filme(self):
        self.lista_filmes()
        id_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme(id_filme)
        if filme:
            novos_dados = self.__tela_filme.pega_dados_filme()
            filme.titulo = novos_dados["titulo"]
            filme.ano = novos_dados["ano"]
            novo_diretor = self.__controlador_sistema.pega_diretor_por_id(novos_dados["id_diretor"])
            filme.diretor = novo_diretor
            
    def lista_filmes(self):
        if not self.__filmes:
            self.__tela_filme.mostra_mensagem("Nenhum filme cadastrado.")
        for filme in self.__filmes:
            self.__tela_filme.mostra_filme({
            "id": filme.id,
            "titulo": filme.titulo,
            "ano": filme.ano,
            "diretor": filme.diretor.nome
                })
            
    def excluir_filme(self):
        self.lista_filmes()
        id_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme(id_filme)
        if filme:
            self.__filmes.remove(filme)
            self.__tela_filme.mostra_mensagem("Filme removido com sucesso.")
        else:
            self.__tela_filme.mostra_mensagem("Filme não encontrado.")
            
    def gerenciar_categorias(self):
        id_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme(id_filme)
        if filme:
            opcao = self.__tela_filme.tela_opcoes_categoria()
            if opcao == 1:
                categoria = self.__controlador_sistema.pega_categoria()
                filme.incluir_categoria(categoria)
            elif opcao == 2:
                nome_cat = self.__tela_filme.pega_nome_categoria()
                filme.remover_categoria(nome_cat)
        else:
            self.__tela_filme.mostra_mensagem("Filme não encontrado.")
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()
            
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_filme, 2: self.alterar_filme,
                         3: self.lista_filmes, 4: self.excluir_filme, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_filme.tela_opcoes()]()