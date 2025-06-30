from DAOs.dao import DAO
from entidade.voto import Voto
from entidade.membro_academia import MembroAcademia
from entidade.categoria import Categoria


class VotoDAO(DAO):
    def __init__(self):
        super().__init__('votos.pkl')

    def add(self, voto: Voto):
        if((voto is not None) and isinstance(voto, Voto) and isinstance(voto.membro, MembroAcademia)):
            super().add((voto.membro.id, voto.categoria.nome), voto)

    def update(self, voto: Voto):
        if((voto is not None) and isinstance(voto, Voto) and isinstance(voto.membro, MembroAcademia)):
            super().update((voto.membro.id, voto.categoria.nome), voto)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
