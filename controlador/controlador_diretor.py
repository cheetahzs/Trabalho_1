from limite.tela_diretor import TelaDiretor
from entidade.diretor import Diretor
from exceptions.diretor_repetido_exception import DiretorRepetidoException


class ControladorDiretor():
    def __init__(self, controlador_sistema):
        self.__diretores = []
        self.__tela_diretor = TelaDiretor()
        self.__controlador_sistema = controlador_sistema

    def pega_diretor(self, id: int):
        for diretor in self.__diretores:
            if diretor.id == id:
                return diretor
        return None
    
    def incluir_diretor(self):
        dados_diretor = self.__tela_diretor.pega_dados_diretor()
        id = dados_diretor["id"]
        adiretortor = self.pega_diretor(id)
        try:
            if diretor == None:
                diretor = Diretor(dados_diretor["id"], dados_diretor["nome"],
                             dados_diretor["data_de_nascimento"], dados_diretor["nacionalidade"])
                self.__diretores.append(diretor)
            else:
                raise AtorRepetidoException(id)
        except AtorRepetidoException as e:
            self.__tela_ator.mostra_mensagem(e)

    def lista_atores(self):
        for ator in self.__atores:
            self.__tela_ator.mostra_ator({"id": ator.id, "nome": ator.nome,
                                         "data_de_nacimento": ator.data_de_nascimento,
                                         "nacionalidade": ator.nacionalidade })
    
    def alterar_ator(self):
        self.lista_atores()
        id_ator = self.__tela_ator.seleciona_ator()
        ator = self.pega_ator(id_ator)

        if(ator is not None):
            novos_dados_ator = self.__tela_ator.pega_dados_ator()
            ator.id = novos_dados_ator["id"]
            ator.nome = novos_dados_ator["nome"]
            ator.data_de_nascimento = novos_dados_ator["data_de_nascimento"]
            ator.nacionalidade = novos_dados_ator["nacionalidade"]
            self.lista_atores()
        else:
            self.__tela_ator.mostra_mensagem("Este ator nao existe")

    def excluir_ator(self):
        self.lista_atores()
        id_ator = self.__tela_ator.seleciona_ator()
        ator = self.pega_ator(id_ator)

        if ator is not None:
            self.__atores.remove(ator)
            self.lista_atores()
        else:
            self.__tela_ator.mostra_mensagem("Este ator nao existe")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_ator, 2: self.alterar_ator,
                         3: self.lista_atores, 4: self.excluir_ator, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_ator.tela_opcoes()]()
