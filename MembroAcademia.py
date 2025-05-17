from abc import ABC, abstractmethod


class(ABC):
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    @abstractmethod
    @property
    def nome(self):
        return self.__nome
    
    @abstractmethod
    @property
    def cpf(self):
        return self.__cpf
    
    @abstractmethod
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @abstractmethod
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf