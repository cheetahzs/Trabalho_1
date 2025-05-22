from votavel import Votavel
from diretor import Diretor


class Filme(Votavel):
    def __init__(self, id, titulo, diretor, ano, categorias):
        super().__init__(id)
        self.__titulo = titulo
        self.__diretor = diretor
        self.__ano = ano
        self.__categorias = []

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def diretor(self):
        return self.__diretor

    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def incluir_categoria(self, categoria):
        if categoria not in self.__categorias:
            self.__categorias.append(categoria)
    
    def remover_categoria(self, nome):
        for categoria in self.__categorias:
            if categoria.nome == nome:
                self.__categorias.remove(categoria)
