from limite.tela_voto import TelaVoto
from entidade.voto import Voto
from exception.voto_repetido_exception import VotoRepetidoException
from entidade.membro_academia import MembroAcademia
from entidade.categoria import Categoria
from collections import defaultdict, Counter


class ControladorVoto():
    def __init__(self, controlador_sistema):
        self.__votos = []
        self.__tela_voto = TelaVoto()
        self.__controlador_sistema = controlador_sistema

    def pega_voto(self, membro: MembroAcademia, categoria: Categoria):
        for voto in self.__votos:
            if voto.membro == membro and voto.categoria == categoria:
                return voto
        return None

    def incluir_voto(self):
        dados_voto = self.__tela_voto.pega_dados_voto()
        membro = dados_voto["membro"]
        categoria = dados_voto["categoria"]
        voto = self.pega_voto(membro, categoria)
        try:
            if voto == None:
                voto = Voto(dados_voto["membro"], dados_voto["categoria"],
                             dados_voto["alvo"])
                self.__votos.append(voto)
            else:
                raise VotoRepetidoException(membro.nome)
        except VotoRepetidoException as e:
            self.__tela_voto.mostra_mensagem(e)

    def lista_votos(self):
        for voto in self.__votos:
            self.__tela_voto.mostra_voto({"membro": voto.membro, "categoria": voto.categoria,
                                         "alvo": voto.alvo})

    def alterar_voto(self):
        self.lista_votos()
        membro_voto, categoria_voto = self.__tela_voto.seleciona_voto()
        voto = self.pega_voto(membro_voto, categoria_voto)

        if(voto is not None):
            novos_dados_voto = self.__tela_voto.pega_dados_voto()
            voto.membro = novos_dados_voto["membro"]
            voto.categoria = novos_dados_voto["categoria"]
            voto.alvo = novos_dados_voto["alvo"]
            self.lista_votos()
        else:
            self.__tela_voto.mostra_mensagem("Este voto nao existe")

    def excluir_voto(self):
        self.lista_votos()
        membro_voto, categoria_voto = self.__tela_voto.seleciona_voto()
        voto = self.pega_voto(membro_voto, categoria_voto)

        if(voto is not None):
            self.__votos.remove(voto)
            self.lista_votos()
        else:
            self.__tela_voto.mostra_mensagem("Este voto nao existe")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def apurar_vencedores(self):
        votos_por_categoria = defaultdict(list)

        for voto in self.__votos:
            votos_por_categoria[voto.categoria].append(voto.alvo)

        vencedores = {}
        for categoria, alvos in votos_por_categoria.items():
            contagem = Counter(alvos)
            mais_votado = contagem.most_common(1)[0]
            vencedores[categoria] = mais_votado

        for categoria, (alvo, qtd_votos) in vencedores.items():
            self.__tela_voto.mostra_mensagem(
                f"Categoria: {categoria.nome} - Vencedor: {alvo.nome} com {qtd_votos} votos")

        return vencedores


    def abre_tela(self):
        lista_opcoes = {1: self.incluir_voto, 2: self.alterar_voto,
                         3: self.lista_votos, 4: self.excluir_voto, 5: self.apurar_vencedores,
                         0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_voto.tela_opcoes()]()
