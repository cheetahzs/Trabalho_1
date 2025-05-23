from membro_academia import MembroAcademia
from categoria import Categoria

class Voto:
    
    def __init__(self, membro: MembroAcademia, categoria: Categoria):
        if isinstance(membro, MembroAcademia):
            self.__membro = membro
        if isinstance(categoria, Categoria):
            self.__categoria = categoria
            
    @property
    def membro(self):
        return self.__membro
    
    @membro.setter
    def membro(self, membro: MembroAcademia):
        if isinstance(membro, MembroAcademia):
            self.__membro = membro
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria: Categoria):
        if isinstance(categoria, Categoria):
            self.__categoria = categoria