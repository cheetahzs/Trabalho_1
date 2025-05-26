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