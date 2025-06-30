from DAOs.dao import DAO
from entidade.ator import Ator


class AtorDAO(DAO):
    def __init__(self):
        super().__init__('atores.pkl')

    def add(self, ator: Ator):
        if((ator is not None) and isinstance(ator, Ator) and isinstance(ator.id, int)):
            super().add(ator.id, ator)

    def update(self, ator: Ator):
        if((ator is not None) and isinstance(ator, Ator) and isinstance(ator.id, int)):
            super().update(ator.id, ator)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
