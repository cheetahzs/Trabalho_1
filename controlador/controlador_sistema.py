from controlador.controlador_filme import ControladorFilme
from controlador.controlador_ator import ControladorAtor
from controlador.controlador_categoria import ControladorCategoria
from controlador.controlador_diretor import ControladorDiretor
from controlador.controlador_voto import ControladorVoto
from limite.tela_sistema import TelaSistema

class controladorSistema:
    
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_filme = ControladorFilme(self)
        self.__controlador_ator = ControladorAtor(self)
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_diretor = ControladorDiretor(self)
        self.__controlador_voto = ControladorVoto(self)
    
    @property    
    def controlador_filme(self):
        return self.__controlador_filme
    
    @property
    def controlador_voto(self):
        return self.__controlador_voto
    
    @property
    def controlador_diretor(self):
        return self.__controlador_diretor
    
    @property
    def controlador_categoria(self):
        return self.__controlador_categoria
    
    @property
    def controlador_ator(self):
        return self.__controlador_ator
        
    def inicializa_sistema(self):
        self.abre_tela()
        
    def abre_tela(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            
            if opcao == 1:
                self.__controlador_ator.abre_tela()
            elif opcao == 2:
                self.__controlador_categoria.abre_tela()
            elif opcao == 3:
                self.__controlador_diretor.abre_tela()
            elif opcao == 4:
                self.__controlador_filme.abre_tela()
            elif opcao == 5:
                self.__controlador_voto.abre_tela()
            elif opcao == 0:
                self.__tela_sistema.mostra_mensagem("Encerrando o sistema...")
                break
            else:
                self.__tela_sistema.mostra_mensagem("Opção inválida!")
                
    def pega_diretor(self, id: int):
        return self.__controlador_diretor.pega_diretor(id)
    
    def pega_categoria(self, nome: str):
        return self.__controlador_categoria.pega_categoria(nome)
    
    def pega_ator(self, id: int):
        return self.__controlador_ator.pega_ator(id)
    
    def pega_filme(self, id: int):
        return self.__controlador_filme.pega_filme(id)