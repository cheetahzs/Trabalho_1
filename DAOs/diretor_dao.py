from DAOs.dao import DAO
from entidade.diretor import Diretor


class DiretorDAO(DAO):
    def __init__(self):
        super().__init__('diretores.pkl')

    def add(self, diretor: Diretor):
        if((diretor is not None) and isinstance(diretor, Diretor) and isinstance(diretor.id, int)):
            super().add(diretor.id, diretor)

    def update(self, diretor: Diretor):
        if((diretor is not None) and isinstance(diretor, Diretor) and isinstance(diretor.id, int)):
            super().update(diretor.id, diretor)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)

    def pega_por_nome(self, nome):
        for diretor in self.get_all():
            if diretor.nome == nome:
                return diretor
        return None
