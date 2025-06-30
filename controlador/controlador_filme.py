from entidade.filme import Filme
from limite.tela_filme import TelaFilme
from exception.filme_repetido_exception import FilmeRepetidoException

class ControladorFilme():
    
    def __init__(self, controlador_sistema):
        self.__filmes = []
        self.__tela_filme = TelaFilme()
        self.__controlador_sistema = controlador_sistema
        
    def pega_filme(self, id: int):
        for filme in self.__filmes:
            if filme.id == id:
                return filme
            
    def incluir_filme(self):
        dados_filme = self.__tela_filme.pega_dados_filme()
        id = dados_filme["id"]
        filme = self.pega_filme(id)
        try: 
            if filme == None:
                filme = Filme(dados_filme["id"], dados_filme["titulo"], 
                              dados_filme["nome_diretor"], dados_filme["ano"])
                self.__filmes.append(filme)
            else:
                raise FilmeRepetidoException(id)
        except FilmeRepetidoException as e:
            self.__tela_filme.mostra_mensagem(e)
    
    def alterar_filme(self):
        self.lista_filmes()
        id_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme(id_filme)
        
        if(filme is not None):
            novos_dados_filme = self.__tela_filme.pega_dados_filme()
            filme.id = novos_dados_filme["id"]
            filme.titulo = novos_dados_filme["titulo"]
            filme.ano = novos_dados_filme["ano"]
            filme.diretor = novos_dados_filme["nome_diretor"]
            self.lista_filmes()
        else:
            self.__tela_filme.mostra_mensagem("Este filme não existe.")
    
    def excluir_filme(self):
        self.lista_filmes()
        id_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme(id_filme)
        
        if filme is not None:
            self.__filmes.remove(filme)
            self.lista_filmes()
        else:
            self.__tela_filme.mostra_mensagem("Este filme não existe.")
            
    def retornar(self):
        return self.__controlador_sistema.abre_tela()
    
    def lista_filmes(self):
        for filme in self.__filmes:
            self.__tela_filme.mostra_filme({"id": filme.id, "titulo": filme.titulo,
                                             "nome_diretor": filme.nome_diretor, "ano": filme.ano})
            
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_filme, 2: self.alterar_filme,
                        3: self.lista_filmes, 4: self.excluir_filme, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_filme.tela_opcoes()]()