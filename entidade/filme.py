from entidade.diretor import Diretor
from entidade.votavel import Votavel

class Filme(Votavel):
    
    def __init__(self, id: int, titulo: str, nome_diretor: Diretor, ano: int):
        super().__init__(id)
        self.__categorias = []
        self.__titulo = titulo
        self.__nome_diretor = nome_diretor
        self.__ano = ano
            
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
          
            
    @property
    def nome_diretor(self):
        return self.__nome_diretor
    
    @nome_diretor.setter
    def nome_diretor(self, diretor: Diretor):
        if isinstance(diretor, Diretor):
            self.__nome_diretor = diretor
            
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, int):
            self.__ano = ano
            
    def incluir_categoria(self, categoria):
        if categoria not in self.__categorias:
            self.__categorias.append(categoria)
    
    def remover_categoria(self, nome):
        for categoria in self.__categorias:
            if categoria.nome == nome:
                self.__categorias.remove(categoria)