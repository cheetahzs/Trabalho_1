from DAOs.dao import DAO
from entidade.categoria import Categoria


class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__('categorias.pkl')

    def add(self, categoria: Categoria):
        if((categoria is not None) and isinstance(categoria, Categoria)):
            super().add(categoria.nome, categoria)

    def update(self, categoria: Categoria):
        if((categoria is not None) and isinstance(categoria, Categoria)):
            super().update(categoria.nome, categoria)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
