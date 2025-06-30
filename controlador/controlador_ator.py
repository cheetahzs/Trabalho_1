from limite.tela_ator import TelaAtor
from entidade.ator import Ator
from exception.ator_repetido_exception import AtorRepetidoException
from DAOs.ator_dao import AtorDAO


class ControladorAtor():
    def __init__(self, controlador_sistema):
        self.__ator_DAO = AtorDAO()
        self.__tela_ator = TelaAtor()
        self.__controlador_sistema = controlador_sistema

    def pega_ator(self, id: int):
        for ator in self.__ator_DAO.get_all():
            print(ator.id)
            if ator.id == id:
                return ator
        return None

    def pega_ator_por_nome(self, nome: str):
        for ator in self.__dao.get_all():
            if ator.nome == nome:
                return ator
        return None

    def incluir_ator(self):
        dados_ator = self.__tela_ator.pega_dados_ator()
        id = dados_ator["id"]
        ator = self.pega_ator(id)
        try:
            if ator == None:
                ator = Ator(dados_ator["id"], dados_ator["nome"],
                             dados_ator["data_de_nascimento"], dados_ator["nacionalidade"])
                self.__ator_DAO.add(ator)
            else:
                raise AtorRepetidoException(id)
        except AtorRepetidoException as e:
            self.__tela_ator.mostra_mensagem(e)

    def lista_atores(self):
        dados_ator = []
        for ator in self.__ator_DAO.get_all():
            dados_ator.append({"id": ator.id, "nome": ator.nome,
                                         "data_de_nascimento": ator.data_nascimento,
                                         "nacionalidade": ator.nacionalidade })
        self.__tela_ator.mostra_ator(dados_ator)

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
            self.__ator_DAO.update(ator)
            self.lista_atores()
        else:
            self.__tela_ator.mostra_mensagem("Este ator nao existe")

    def excluir_ator(self):
        self.lista_atores()
        id_ator = self.__tela_ator.seleciona_ator()
        ator = self.pega_ator(id_ator)

        if ator is not None:
            self.__ator_DAO.remove(ator.id)
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
